import pygame
import gtk
import Queue
import thread

# This module reuses Pygame's Event, but
# reimplements the event queue.
from pygame.event import Event, event_name, pump as pygame_pump

#print "Initializing own event.py"

# Install myself on top of pygame.event
def install():
    """Installs this module (eventwrap) as an in-place replacement for the pygame.event module. Use install() when you need to interact with unaware Pygame code, forcing it to use this module's event queue."""
    import eventwrap,pygame
    pygame.event = eventwrap
    import sys
    sys.modules["pygame.event"] = eventwrap
    

# Event queue:
g_events = Queue.Queue()

# Set of blocked events as set by set
g_blocked = set()
g_blockedlock = thread.allocate_lock()
g_blockAll = False

def pump():
    """Handle any window manager and other external events that aren't passed to the user. Call this periodically (once a frame) if you don't call get(), poll() or wait()."""
    pygame_pump()

def get():
    """Get a list of all pending events. (Unlike pygame, there's no option to filter by event type; you should use set_blocked() if you don't want to see certain events.)"""
    pump()
    eventlist = []
    try:
        while True:
            eventlist.append(g_events.get(block=False))
    except Queue.Empty:
        pass

    return eventlist

def poll():
    """Get the next pending event if exists. Otherwise, return pygame.NOEVENT."""
    pump()
    try:
        return g_events.get(block=False)
    except Queue.Empty:
        return Event(pygame.NOEVENT)


def wait():
    """Get the next pending event, waiting if none."""
    pump()
    return g_events.get(block=True)

def peek(types=None):
    """True if there is any pending event. (Unlike pygame, there's no option to
    filter by event type)"""
    return not g_events.empty()
    
def clear():
    """Dunno why you would do this, but throws every event out of the queue"""
    try:
        while True:
            g_events.get(block=False)
    except Queue.Empty:
        pass

def set_blocked(item):
    g_blockedlock.acquire()
    try:
        # FIXME: we do not currently know how to block all event types when
        # you set_blocked(none).
        [g_blocked.add(x) for x in makeseq(item)]
    finally:
        g_blockedlock.release()
    
def set_allowed(item):
    g_blockedlock.acquire()
    try:
        if item is None:
            # Allow all events when you set_allowed(none). Strange, eh?
            # Pygame is a wonderful API.
            g_blocked.clear()
        else:
            [g_blocked.remove(x) for x in makeseq(item)]
    finally:
        g_blockedlock.release()

def get_blocked(*args, **kwargs):
    g_blockedlock.acquire()
    try:
        blocked = frozenset(g_blocked)
        return blocked
    finally:
        g_blockedlock.release()

def set_grab(grabbing):
    # We don't do this.
    pass

def get_grab():
    # We don't do this.
    return False

def post(event):
    #print "posting on own"
    g_blockedlock.acquire()
    try:
        if event.type not in g_blocked:
            g_events.put(event, block=False)
    finally:
        g_blockedlock.release()

def makeseq(obj):
    """Accept either a scalar object or a sequence, and return a sequence
    over which we can iterate. If we were passed a sequence, return it
    unchanged. If we were passed a scalar, return a tuple containing only
    that scalar. This allows the caller to easily support one-or-many.
    """
    # Strings are the exception because you can iterate over their chars
    # -- yet, for all the purposes I've ever cared about, I want to treat
    # a string as a scalar.
    if isinstance(obj, basestring):
        return (obj,)
    try:
        # Except as noted above, if you can get an iter() from an object,
        # it's a collection.
        iter(obj)
        return obj
    except TypeError:
        # obj is a scalar. Wrap it in a tuple so we can iterate over the
        # one item.
        return (obj,)
