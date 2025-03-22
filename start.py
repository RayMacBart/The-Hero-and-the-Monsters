try:
#   import pygame_sdl2
#   pygame_sdl2.import_as_pygame()
    import pygame
    import sys
    import os
    import traceback
except ModuleNotFoundError:
    print('imports at main: ModuleNotFoundError')
except ImportError:
    print('imports at main: ImportError')
except:
    print('imports at main: unknown Error')
	
pygame.init()

if os.path.isdir('data'):
    pass
else:
    os.mkdir('data')

sys.path.append('data')
sys.path.append('data/levels')
	
if os.path.isfile('data/mainloop.py'):
    import mainloop
else:
    print('no mainloop!')
	
pygame.key.start_text_input()
pygame.key.stop_text_input()
try:
    mainloop.rootfunction()
except Exception:
    traceback.print_exc()
    pygame.quit()

pygame.quit()
