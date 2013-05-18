import init, pygame, graphics, sys

from pygame.locals import *

default_max_fps = 60

def main():
    gfx = init.init_pygame(None)

    # stage = Title()

    gfx.set_font(18)

    dims = gfx.get_dimensions()

    white = (255,255,255)



    while True:
        gfx.update()
        gfx.draw()
        gfx.flip()

    init.finish_pygame()

if __name__ == '__main__':
    main()
