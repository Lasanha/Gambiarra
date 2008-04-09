import pango
import cairo
import pangocairo
import pygame.rect, pygame.image
import gtk
import struct
from pygame import surface

# Install myself on top of pygame.font
def install():
    import pangofont,pygame
    pygame.font = pangofont
    import sys
    sys.modules["pygame.font"] = pangofont

class PangoFont(object):
    """Base class for a pygame.font.Font-like object drawn by Pango."""
    def __init__(self, family=None, size=None, bold=False, italic=False, fd=None):
        """If you know what pango.FontDescription (fd) you want, pass it in as
        'fd'.  Otherwise, specify any number of family, size, bold, or italic,
        and we will try to match something up for you."""

        # Always set the FontDescription (FIXME - only set it if the user wants
        # to change something?)
        if fd is None:
            fd = pango.FontDescription()
            if family is not None:
                fd.set_family(family)
            if size is not None:
                fd.set_size(size*1000)

            if bold:
                fd.set_weight(pango.WEIGHT_BOLD)
            if italic:
                fd.set_style(pango.STYLE_OBLIQUE)

        self.fd = fd

    def render(self, text, antialias, color, background=None):
        """Render the font onto a new Surface and return it.
        We ignore 'antialias' and use system settings.
        NOTE: Due to a retarded implementation problem you cannot use 
        transparent colors. Alpha is ignored (set to 255)."""

        # create layout
        layout = pango.Layout(gtk.gdk.pango_context_get())
        layout.set_font_description(self.fd)
        layout.set_text(text)

        # determine pixel size
        (logical, ink) = layout.get_pixel_extents()
        ink = pygame.rect.Rect(ink)

        # Create a new Cairo ImageSurface
        csrf = cairo.ImageSurface(cairo.FORMAT_ARGB32, ink.w, ink.h)
        cctx = pangocairo.CairoContext(cairo.Context(csrf))

        # Mangle the colors on little-endian machines. The reason for this 
        # is that Cairo writes native-endian 32-bit ARGB values whereas
        # Pygame expects endian-independent values in whatever format. So we
        # tell our users not to expect transparency here (avoiding the A issue)
        # and we swizzle all the colors around.
        big_endian = ((1,) == struct.unpack("=i","\0\0\0\001"))
        def mangle_color(color):
            if len(color) not in [3,4]:
                raise ArgumentError("expected a 3- or 4-integer-tuple for color")
            if big_endian:
                # Big-endian; leave
                return (color[0]/255.0,color[1]/255.0,color[2]/255.0,1.0)
            else:
                # Little-endian; swizzle
                return (color[2]/255.0,color[1]/255.0,color[0]/255.0,1.0)

        # render onto it
        if background is not None:
            cctx.set_source_rgba(*mangle_color(background))
            cctx.paint()

        cctx.new_path()
        cctx.layout_path(layout)
        cctx.set_source_rgba(*mangle_color(color))
        cctx.fill()

        # Create and return a new Pygame Image derived from the Cairo Surface
        if big_endian:
            # You see, in big-endian-world, we can just use the RGB values
            format = "ARGB"
        else:
            # But with little endian, we've already swapped R and B in 
            # mangle_color, so now just move the A
            format = "RGBA"
        return pygame.image.fromstring(str(csrf.get_data()), (ink.w,ink.h), format)


class SysFont(PangoFont):
    """Construct a PangoFont from a font description (name), size in pixels,
    bold, and italic designation. Similar to SysFont from Pygame."""
    def __init__(self, name, size, bold=False, italic=False):
        fd = pango.FontDescription(name)
        fd.set_absolute_size(size*pango.SCALE)
        if bold:
            fd.set_weight(pango.WEIGHT_BOLD)
        if italic:
            fd.set_style(pango.STYLE_OBLIQUE)
        super(SysFont, self).__init__(fd=fd)

class NotImplemented(Exception):
    pass

class Font(PangoFont):
    def __init__(self, *args, **kwargs):
        raise NotImplemented("PangoFont doesn't support Font directly, use SysFont or .fontByDesc")

def match_font(name,bold=False,italic=False):
    raise NotImplemented("PangoFont doesn't support match_font directly, use SysFont or .fontByDesc")

def fontByDesc(desc="",bold=False,italic=False):
    """Constructs a FontDescription from the given string representation.
The format of the string representation is:

  "[FAMILY-LIST] [STYLE-OPTIONS] [SIZE]"

where FAMILY-LIST is a comma separated list of families optionally terminated by a comma, STYLE_OPTIONS is a whitespace separated list of words where each WORD describes one of style, variant, weight, or stretch, and SIZE is an decimal number (size in points). For example the following are all valid string representations:

  "sans bold 12"
  "serif,monospace bold italic condensed 16"
  "normal 10"

The commonly available font families are: Normal, Sans, Serif and Monospace. The available styles are:
Normal	the font is upright.
Oblique	the font is slanted, but in a roman style.
Italic	the font is slanted in an italic style.

The available weights are:
Ultra-Light	the ultralight weight (= 200)
Light	the light weight (=300)
Normal	the default weight (= 400)
Bold	the bold weight (= 700)
Ultra-Bold	the ultra-bold weight (= 800)
Heavy	the heavy weight (= 900)

The available variants are:
Normal	
Small-Caps	

The available stretch styles are:
Ultra-Condensed	the smallest width
Extra-Condensed	
Condensed	
Semi-Condensed	
Normal	the normal width
Semi-Expanded	
Expanded	
Extra-Expanded	
Ultra-Expanded	the widest width
    """
    fd = pango.FontDescription(name)
    if bold:
        fd.set_weight(pango.WEIGHT_BOLD)
    if italic:
        fd.set_style(pango.STYLE_OBLIQUE)
    return PangoFont(fd=fd)

def get_init():
    return True

def init():
    pass

def quit():
    pass

def get_default_font():
    return "sans"

def get_fonts():
    return ["sans","serif","monospace"]


def stdcolor(color):
    def fixlen(color):
        if len(color) == 3:
            return tuple(color) + (255,)
        elif len(color) == 4:
            return color
        else:
            raise TypeError("What sort of color is this: %s" % (color,))

    def fixbase(color):
        return [x/255.0 for x in color]

    return fixbase(fixlen(color))
