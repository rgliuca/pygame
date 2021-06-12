import pygame

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Animate Objects")
rect = pygame.Rect(300, 100, 100, 100)
green = (0, 255, 0) # (R, G, B)
blue = (0, 0, 255)

x = 0
y = 0
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
    
    #screen.fill((255, 255, 255))

    pygame.font.init() 
    font = pygame.font.SysFont('Comic Sans MS', 30)    
    text_surface = font.render('Hello World', False, (255, 0, 0))
    screen.blit(text_surface, (100, 100))

    pygame.draw.line(screen, (0, 255, 0), (200, 200), (400, 400))

    pygame.draw.circle(screen, (0,0,0), (100 + x, 100 + y), 50)
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_UP]:
        y -= 0.25
    elif key_pressed[pygame.K_DOWN]:
        y += 0.25 
    elif key_pressed[pygame.K_LEFT]:
        x -= 0.25
    elif key_pressed[pygame.K_RIGHT]:
        x += 0.25
    elif key_pressed[pygame.K_q]:
        exit()
    pygame.draw.circle(screen, green, (100 + x, 100 + y), 50)
    pygame.draw.rect(screen, blue, rect, 5)
    pygame.display.flip()

pygame.quit()

