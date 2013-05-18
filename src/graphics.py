import pygame, error, datetime

from static_var import static_var
from pygame.locals import *
from collections import *

import phase, time

from exit_listener import ExitListener

import xml.etree.cElementTree as ET

class Graphics(object):
    Point = namedtuple('Point', 'x y')
    Rectangle = namedtuple('Rectangle', 'x y w h')

    default_color = pygame.Color('black')
    default_bg = pygame.Color('white')

    def __init__(self, phase_xml):
        fails = pygame.init()[1]

        if fails > 0:
            error.fatal()

        try:
            self.screen = pygame.display.set_mode((0,0), FULLSCREEN|DOUBLEBUF)
        except pygame.error as e:
            error.fatal(e)

        self.set_font()

        self.fps = 0
        self.frames = 0
        self.last_second = datetime.datetime.now()
        self.phase = phase.Phase(self, [ExitListener()], None)
        self.max_fps = 0

    def bounds_check(self, pos):
        return error.assert_smell(rect_contains(self.phase.get_size(), pos), 'Object does not fit within bounds. (pos={0}, size={1})'.format(pos, self.phase.get_size()))

    def clear(self, color):
        self.screen.fill(color)

    def blit(self, obj, pos):
        if self.bounds_check(pos):
            self.screen.blit(obj, pos)

    def update(self):
        if self.get_fps() == 0:
            self.phase.update()
        else:
            start_t = datetime.datetime.now()
            self.phase.update()
            end_t = datetime.datetime.now()

            actual = ((end_t - start_t).total_seconds())

            sleep = 1 / (self.max_fps - actual)

            if sleep > 0:
                time.sleep(sleep)

    def draw(self):
        self.phase.draw()

    def set_font(self, size=12, name=None):
        if name == None:
            self.font = pygame.font.SysFont(name, size)
        else:
            # Find a better method of default font selection...
            self.font = pygame.font.SysFont(pygame.font.get_fonts()[0], size)

    def measure(self, font, string):
        return font.measure(size)

    def flip(self):
        pygame.display.flip()

    def get_screen_dimensions(self):
        return (self.screen.get_width(), self.screen.get_height())

    def get_dimensions(self):
        return self.phase.get_size()

    def center(self, obj, **keywords):
        if 'x' in keywords:
            x = keywords['x']
        else:
            # Use integer division in case some freaky future monitor doesn't have a resolution that's divisible by two.
            x = (self.screen.get_width() - obj.get_width()) // 2
        if 'y' in keywords:
            y = keywords['y']
        else:
            y = (self.screen.get_height() - obj.get_height()) // 2;

        return Graphics.Point(x, y)

    def render_str(self, to_render, color=default_color, **keywords):
        obj = self.font.render(to_render, True, color)
        self.blit(obj, self.center(obj, **keywords))
        # print 'rendered', to_render, 'in color', color, 'at', self.center(obj, **keywords)

    def draw_circle(self, radius, pos, color=default_color, stroke=1):
        if self.bounds_check(pos):
            if stroke < 1:
                error.fatal("Could not draw circle at {0}...".format(pos))
                pygame.draw.circle(self.screen, color, pos, radius, stroke)

    def fill_circle(self, radius, pos, color=default_color):
        if self.bounds_check(pos):
            pygame.draw.circle(self.screen, color, pos, radius, 0)

    def get_fps(self):
        now = datetime.datetime.now()
        if (now - self.last_second).total_seconds() >= 1.0:
            self.fps = self.frames
            self.frames = 0
            self.last_second = now
        else:
            self.frames += 1
            return self.fps

def rect_contains(rect, pos):
        return rect.collidepoint(pos)
def mk_rect(x,y,w,h):
    return pygame.Rect(x,y,w,h)
