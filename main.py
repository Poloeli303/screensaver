import pygame
pygame.init()

screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("The best Pong ever")


bx = 350
by = 250
bVx = 3
bVy = 3




doExit = False
clock = pygame.time.Clock()
while not doExit:
    clock.tick(60)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
           

    bx += bVx
    by += bVy
   


    if bx < 0 or bx + 20 > 560:
        bVx *= -1
    if by < 0 or by + 20 > 470:
        bVy *= -1




#___________________________________RENDER SECTION____________________________________________________
    screen.fill((0,0,0))
    font = pygame.font.Font(None, 74)
    text = font.render(str("Apple"),1, (0, 0, 250))
    screen.blit(text, (bx, by))
    pygame.display.flip()
pygame.quit()
