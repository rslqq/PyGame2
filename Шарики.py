import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

radius = 10
speed = 10

sp = []

fin = True

while fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            sp.append([pos[0], pos[1], speed / math.sqrt(2), -speed / math.sqrt(2)])

    screen.fill('black')

    for f in sp:
        pygame.draw.circle(screen, (255, 255, 255), [int(f[0]), int(f[1])], radius)
        f[0] -= f[2] / 60
        f[1] += f[3] / 60
        if f[0] < radius or f[0] > 800 - radius:
            f[2] = -f[2]
        if f[1] < radius or f[1] > 600 - radius:
            f[3] = -f[3]

    pygame.display.flip()

pygame.quit()
