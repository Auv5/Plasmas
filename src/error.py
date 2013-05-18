import pygame, sys, inspect, datetime

log = open("plasmas.log", "a+")

def assert_fatal(cond, e):
    if not cond:
        fatal(e)

def assert_smell(cond, e):
    if not cond:
        smell(e)
        return False
    else:
        return True

def fatal(e=None):
    if e is None:
        pygame_error = pygame.get_error()
    else:
        pygame_error = str(e)

    stack_from = inspect.stack()[1]

    mod = inspect.getmodule(stack_from[0])

    if mod == sys.modules[__name__]:
        stack_from = inspect.stack()[2]
        mod = inspect.getmodule(stack_from[0])


    print(mod, sys.modules[fatal.__module__])
    print('[ERROR] {0} ({1} function {2} line {3}). See log for more details.'
          .format(pygame_error, stack_from[1], stack_from[3], stack_from[2]))


    if isinstance(e, Exception):
        log.write('\n[{0}] [ERROR] {1}\nTraceback:\n{2}'.format(str(datetime.datetime.now()), str(e), traceback.format_exc()))
    else:
        log.write('\n[{0}] [ERROR] {1}'.format(str(datetime.datetime.now()), str(e)))

    # Indicate failure.
    sys.exit(1)

# Defines a potential bug condition. Writes to STDOUT about it.
# (Since smells aren't usually caused by exceptions or SDL errors
# , the e argument is mandatory.
def smell(e):
    stack_from = inspect.stack()[1]

    mod = inspect.getmodule(stack_from[0])

    if mod == sys.modules[__name__]:
        stack_from = inspect.stack()[2]
        mod = inspect.getmodule(stack_from[0])

    print('[SMELL] {0} ({1} function {2} line {3})'
          .format(str(e), stack_from[1], stack_from[3], stack_from[2]))

    log.write('\n[{0}] [SMELL] {1}'.format(str(datetime.datetime.now()), str(e)))
