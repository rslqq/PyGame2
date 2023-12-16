import pygame
import random

pygame.init()

size = width, height = random.randint(300, 500), random.randint(300, 500)
screen = pygame.display.set_mode(size)

fin = True
flag = False

x, y = 0, 0

size_cir = 0

blue = pygame.Color('blue')
clock = pygame.time.Clock()

while fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            size_cir = 0
            flag = True
    screen.fill(blue)
    if flag:
        pygame.draw.circle(screen, 'yellow', (x, y), size_cir, 0)
        size_cir += 1
    clock.tick(100)
    pygame.display.flip()
pygame.quit()