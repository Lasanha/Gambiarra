import os
import sys
import threading
from pprint import pprint

import pygtk
pygtk.require('2.0')
import gtk
import gobject
import pygame

import gtkEvent

import video

__all__ = ['PyGameCanvas']

class PyGameCanvas(gtk.EventBox):
    def __init__(self, width, height):

        # Build the main widget
        super(PyGameCanvas,self).__init__()
        
        # Build the sub-widgets
        self._align = gtk.Alignment(0.5, 0.5)
        self._inner_evb = gtk.EventBox()
        self._socket = gtk.Socket()

        
        # Add internal widgets
        self._inner_evb.set_size_request(width, height)
        self._inner_evb.add(self._socket)
        self._socket.show()
        
        self._align.add(self._inner_evb)
        self._inner_evb.show()
        
        self._align.show()
        
        self.add(self._align)

        # Construct a gtkEvent.Translator
        self._translator = gtkEvent.Translator(self, self._inner_evb)
        
        # <Cue Thus Spract Zarathustra>
        self.set_flags(gtk.CAN_FOCUS)
        self.show()
        
    def connect_game(self, app):
        # Setup the embedding
        os.environ['SDL_WINDOWID'] = str(self._socket.get_id())
        #print 'Socket ID=%s'%os.environ['SDL_WINDOWID']
        pygame.init()

        self._translator.hook_pygame()
        
        # Load the modules
        # NOTE: This is delayed because pygame.init() must come after the embedding is up
        if ':' not in app:
            app += ':main'
        mod_name, fn_name = app.split(':')
        mod = __import__(mod_name, globals(), locals(), [])
        fn = getattr(mod, fn_name)
        
        # Start Pygame
        self.__thread = threading.Thread(target=self._start, args=[fn])
        self.__thread.start()

    def _start(self, fn):
        import olpcgames
        olpcgames.widget = self
        import sugar.activity.activity,os
        os.chdir(sugar.activity.activity.get_bundle_path())
        
        try:
            fn()
        finally:
            gtk.main_quit()
        
