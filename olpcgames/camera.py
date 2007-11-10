import threading
import time
import os

import pygame
import gst

import video

class CameraSprite(object):
    """Create gstreamer surface for the camera."""
    
    def __init__(self, x, y):
        import olpcgames
        if olpcgames.widget:
            self._init_video(olpcgames.widget, x, y)
            
    def _init_video(self, widget, x, y):
        self._vid = video.VideoWidget()
        widget._fixed.put(self._vid, x, y)
        self._vid.show()
        
        self.player = video.Player(self._vid)
        self.player.play()
        
class Camera(object):
    """A class representing the camera."""
    
    def __init__(self):
        self.pipe = gst.parse_launch('v4l2src ! ffmpegcolorspace ! pngenc ! filesink location="/tmp/snap.png"')
        self.bus = self.pipe.get_bus()

    def snap(self):
        print 'Starting snap'
        self.pipe.set_state(gst.STATE_PLAYING)
        #while True:
        #    evt = self.bus.poll(gst.MESSAGE_ANY, -1)
        #    print 'Event %s %r'%(evt.type, evt)
        #    os.system('du -hcs /tmp/snap.png')
        tmp = False
        while True:
            evt = self.bus.poll(gst.MESSAGE_STATE_CHANGED, -1)
            old, new, pending = evt.parse_state_changed()
            if pending == gst.STATE_VOID_PENDING:
                if tmp:
                    break
                else:
                    tmp = True
        print 'Ending snap'
        
        return pygame.image.load('/tmp/snap.png')
        
def snap():
    """Dump a snapshot from the camera to a pygame surface."""

    pipe = gst.parse_launch('v4l2src ! ffmpegcolorspace ! pngenc ! filesink location="/tmp/snap.png"')
    bus = pipe.get_bus()
    cond = threading.Condition()
    cond.acquire()
    
    def _msg(bus, message):
        t = message.type
        if t == gst.MESSAGE_EOS:
            cond.acquire()
            cond.notify()
            cond.release()
    bus.connect('message', _msg)
    
    def _snap():
        pipe.set_state(gst.STATE_PLAYING)
        
    t = threading.Thread(target=_snap)
    t.start()
    cond.wait()
            
    return pygame.image.load('/tmp/snap.png')