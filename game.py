from vector import Vector
import pygame


class Player:
    def __init__(self, x, y):
        self.pos = Vector(x, y)


class Enemy:
    def __init__(self, x, y):
        self.pos = Vector(x, y)
        self.R = 50
        self.v = 2

    def move(self, player):
        v = self.v * (player.pos - self.pos).normalize()
        self.pos += v

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.pos.x), int(self.pos.y)), self.R)

    def update(self, screen, player):
        self.move(player)
        self.draw(screen)
