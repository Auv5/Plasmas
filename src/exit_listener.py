import sys, pygame
from pygame.locals import *
from keyboardlistener import KeyboardListener

class ExitListener(KeyboardListener):
    def __init__(self):
        KeyboardListener.__init__(self, [K_ESCAPE])

    def key_pressed(self, keyno):
        # We don't need to worry about any other key because this is the only one we registered...
        sys.exit(0)
