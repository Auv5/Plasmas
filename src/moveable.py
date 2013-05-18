import pygame, graphics, error

from pygame.locals import *

from keyboardlistener import KeyboardListener

class Moveable(KeyboardListener):
    def __init__(self, gfx, pos):
        self.dx = 0
        self.dy = 0

        self.pos = pos
        self.spawn = pos[:]

        self.gfx = gfx

        KeyboardListener.__init__(self, [K_w, K_a, K_s, K_d])

    def key_pressed(self, key):
        if key == K_w:
            # JUMP
            self.dy -= 1
        if key == K_s:
            # Don't know what to do here...
            self.dy += 1
        if key == K_a:
            self.dx -= 1
        if key == K_d:
            self.dx += 1

    def key_up(self, key):
        # if key == K_w:
        #     # Nothing really.
        #     pass
        # if key == K_s:
        #     pass

        if key == K_w:
            self.dy += 1
        if key == K_s:
            self.dy -= 1
        if key == K_a:
            self.dx += 1
        if key == K_d:
            self.dx -= 1

    def update(self):
        dimensions = self.gfx.get_dimensions()

        if self.dx < 0 and self.pos.x > dimensions.x:
            self.pos.x += self.dx
        if self.dx > 0 and self.pos.x < dimensions.w:
            self.pos.x += self.dx
        if self.dy > 0 and self.pos.y < dimensions.h:
            self.pos.y += self.dy
        if self.dy < 0 and self.pos.y > dimensions.y:
            self.pos.y += self.dy

    def register(self, phase):
        phase.keylisteners.append(self)
        phase.entities.append(self)

    def draw(self, gfx):
        to_render = 'dx = {0} dy = {1} pos = {2} fps = {3}'.format(self.dx, self.dy, self.pos, gfx.fps)
        gfx.render_str(to_render)
        gfx.fill_circle(2, self.pos)
