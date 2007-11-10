import pygtk
pygtk.require('2.0')
import gtk
import hippo

from sugar.activity import activity
from sugar.graphics import style
from olpcgames.canvas import PyGameCanvas

import mesh

__all__ = ['PyGameActivity']

class PyGameActivity(activity.Activity):
        
    game_name = None
    game_title = 'PyGame Game'
    game_handler = None
    game_size = (16 * style.GRID_CELL_SIZE,
                 11 * style.GRID_CELL_SIZE)
    pygame_mode = 'SDL'
        
    def __init__(self, handle):
            super(PyGameActivity, self).__init__(handle)
            
            self.set_title(self.game_title)
            
            toolbar = activity.ActivityToolbar(self)
            toolbar.show()
            self.set_toolbox(toolbar)
            def shared_cb(*args, **kwargs):
                mesh.activity_shared(self)
            def joined_cb(*args, **kwargs):
                mesh.activity_joined(self)
            self.connect("shared", shared_cb)
            self.connect("joined", joined_cb)

            if self.get_shared():
                # if set at this point, it means we've already joined (i.e.,
                # launched from Neighborhood)
                joined_cb()

            toolbar.title.unset_flags(gtk.CAN_FOCUS)
            
            assert self.game_handler or self.game_name, 'You must specify a handler module (%r)'%(self.game_handler or self.game_name)

            if self.pygame_mode != 'Cairo':

                self._pgc = PyGameCanvas(*self.game_size)
                self.set_canvas(self._pgc)
                self._pgc.grab_focus()
                self._pgc.connect_game(self.game_handler or self.game_name)
                gtk.gdk.threads_init()

            else:
                self._drawarea = gtk.DrawingArea()
                canvas = hippo.Canvas()
                canvas.grab_focus()
                self.set_canvas(canvas)
                self.show_all()

                import pygamecairo
                pygamecairo.install()

                pygamecairo.display.init(canvas)
                app = self.game_handler or self.game_name
                if ':' not in app:
                    app += ':main'
                mod_name, fn_name = app.split(':')
                mod = __import__(mod_name, globals(), locals(), [])
                fn = getattr(mod, fn_name)
                fn()

