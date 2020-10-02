from vector import Vector
import game
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
e = game.Enemy(100, 100)
p = game.Player(800, 600)

running = True
while running:
    screen.fill((200, 200, 200))
    e.update(screen, p)
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

