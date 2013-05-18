import pygame, graphics

from pygame.locals import *

def init_pygame(phase):
    gfx = graphics.Graphics(phase)

    return gfx

def finish_pygame():
    pygame.quit()
