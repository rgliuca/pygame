import pygame

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Draw Basic Objects")
GREEN = (0, 255, 0) # (R, G, B)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break

    '''
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_q]:
        done = True
    '''
    #screen.fill((255, 255, 255))
    pygame.draw.line(screen, GREEN, (200, 200), (400, 400))
    pygame.draw.circle(screen, RED, (400, 200), 50, 0)
    pygame.draw.rect(screen, BLUE, pygame.Rect(300, 200, 350, 250), 5)

    pygame.display.flip()

pygame.quit()

