import keyboardlistener
import graphics, pygame, moveable
from pygame.locals import *


class Phase(object):
    def __init__(self, gfx, kls, size):
        self.keylisteners = kls
        self.gfx = gfx
        self.size = graphics.mk_rect(0, 0, *gfx.get_screen_dimensions())
        self.entities = []
        moveable.Moveable(gfx, graphics.Graphics.Point(10,10)).register(self)

    def get_size(self):
        return self.size

    def update(self):
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                for k in self.keylisteners:
                    k.key(event.key)
            if event.type == KEYUP:
                for k in self.keylisteners:
                    k.key_up(event.key)
        for e in self.entities:
            e.update()

    def draw(self):
        self.gfx.clear(self.gfx.default_bg)
        for e in self.entities:
            e.draw(self.gfx)
