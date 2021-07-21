import pygame
from pygame.locals import KEYDOWN

width  = 800 
height = 600
size   = [width, height]
pygame.init()
screen = pygame.display.set_mode(size)
background = pygame.Surface(screen.get_size())

b = pygame.sprite.Sprite() # create sprite
b.image = pygame.image.load("mine.png").convert() # load ball image
b.rect = b.image.get_rect() # use image extent values
b.rect.topleft = [0, 100] # put the ball in the top left corner

pygame.display.update()

while pygame.event.poll().type != KEYDOWN:
	screen.blit(b.image, b.rect)
	b.rect.topleft = [0, 100]
	pygame.time.delay(1)
	pygame.display.update()
