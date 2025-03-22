import pygame
pygame.init()
a = 1
pygame.display.init()
size = [640, 400]   
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
while a == 1:
	for e in pygame.event.get():
		if e.type == pygame.KEYUP:
			if e.key == pygame.K_a:
				a = 2
				pygame.quit()
			else:
				print(e.key)
