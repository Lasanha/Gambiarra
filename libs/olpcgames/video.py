import os
import signal

import pygtk
pygtk.require('2.0')
import gtk
import logging
import gst

class VideoWidget(gtk.DrawingArea):
    """A custom widget to render GStreamer video."""
    
    def __init__(self, x=160, y=120):
        super(VideoWidget, self).__init__()
        self._imagesink = None
        self.unset_flags(gtk.DOUBLE_BUFFERED)
        self.set_size_request(x,y)

    def do_expose_event(self, event):
        if self._imagesink:
            self._imagesink.expose()
            return False
        else:
            return True

    def set_sink(self, sink):
        assert self.window.xid
        self._imagesink = sink
        self._imagesink.set_xwindow_id(self.window.xid)
        
#pipe_desc = 'v4l2src ! video/x-raw-yuv,width=160,height=120 ! ffmpegcolorspace ! xvimagesink'
pipe_desc = 'v4l2src ! ffmpegcolorspace ! video/x-raw-yuv ! xvimagesink'
class Player(object):
    def __init__(self, videowidget):
        self._playing = False
        self._videowidget = videowidget

        self._pipeline = gst.parse_launch(pipe_desc)

        bus = self._pipeline.get_bus()
        bus.enable_sync_message_emission()
        bus.add_signal_watch()
        bus.connect('sync-message::element', self.on_sync_message)
        bus.connect('message', self.on_message)

    def play(self):
        if self._playing == False:
            self._pipeline.set_state(gst.STATE_PLAYING)
            self._playing = True

    def pause(self):
        if self._playing == True:
            self._pipeline.set_state(gst.STATE_PAUSED)
            self._playing = False

    def on_sync_message(self, bus, message):
        if message.structure is None:
            return
        if message.structure.get_name() == 'prepare-xwindow-id':
            self._videowidget.set_sink(message.src)

    def on_message(self, bus, message):
        t = message.type
        if t == gst.MESSAGE_ERROR:
            err, debug = message.parse_error()
            logging.debug("Video error: (%s) %s" % (err, debug))
            self._playing = False
            gtk.main_quit()
    