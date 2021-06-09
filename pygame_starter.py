import pygame

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Draw Basic Objects")
green = (0, 255, 0) # (R, G, B)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
    
    #screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0, 255, 0), (200, 200), (400, 400))

    pygame.display.flip()

