import pygame

pygame.init()

screen = pygame.display.set_mode((200, 200))

font = pygame.font.Font(None, 100)
text_surface = font.render("1", True, (255, 0, 0))

ch = 1

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.ACTIVEEVENT:
            if event.state == pygame.APPACTIVE and event.gain == 0:
                ch += 1
                text_surface = font.render(str(ch), True, (255, 0, 0))

    screen.fill('black')

    screen.blit(text_surface, (50, 50))

    pygame.display.update()

pygame.quit()