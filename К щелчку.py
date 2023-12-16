import pygame


size = width, height = 501, 501
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

White = pygame.Color((255, 0, 0))

x, y = 251, 251
x1, y1 = x, y

run = True

while run:
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, White, (x, y), 20)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos[0], event.pos[1]
        if event.type == pygame.QUIT:
            run = False

    if x1 > x:
        x += 1
    elif x1 < x:
        x -= 1

    if y1 > y:
        y += 1
    elif y1 < y:
        y -= 1

    pygame.display.flip()

    clock.tick(60)

pygame.quit()