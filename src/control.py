import error
from keyboardlistener, mouselistener import *

class Control(KeyboardListener, MouseListener):
    def __init__(self, bounds):
        error.assert_fatal(bounds != None, "Control requires bounds.")
        KeyboardListener.__init__([])
        MouseListener.__init__()
        self.bounds = bounds;
    def get_height():
        return self.bounds.h

    def get_width():
        return self.bounds.w
