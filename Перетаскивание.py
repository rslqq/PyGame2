import pygame

pygame.init()

size = width, height = 300, 300
screen = pygame.display.set_mode(size)

fin = True
move = False

x, y = 0, 0

x_n, y_n = 0, 0

while fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if x < event.pos[0] < x + 100 and y < event.pos[1] < y + 100:
                move = True
        if event.type == pygame.MOUSEMOTION:
            if move:
                x_n, y_n = event.rel
                x, y = x + x_n, y + y_n
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            move = False

    pygame.draw.rect(screen, 'green', (x, y, 100, 100))

    pygame.display.flip()
    screen.fill('black')

pygame.quit()