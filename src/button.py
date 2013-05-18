import graphics, control

class Button(control.Control):
    def __init__(self, **keywords):
        pass

def mk_phase_change(phase):
    def change(gfx):
        gfx.phase_shift(phase)
