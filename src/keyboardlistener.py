class KeyboardListener(object):
    def __init__(self, keys):
        self.keys = keys
    def key(self, keyno):
        if keyno in self.keys:
            return self.key_pressed(keyno)
        else:
            return False
    def key_up(self, keyno):
        if keyno in self.keys:
            return self.key_up(keyno)
        else:
            return False
