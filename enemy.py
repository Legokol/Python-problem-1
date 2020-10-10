import pygame
from pygame import gfxdraw


class Enemy:
    def __init__(self, x, y, v, r):
        self.pos = pygame.math.Vector2(x, y)
        self.v = v
        self.r = r

    def move(self, player):
        v = self.v * (player.pos - self.pos).normalize()  # following the player with own speed
        self.pos += v

    def collision(self, player):
        return (self.pos - player.pos).magnitude() < self.r + player.r

    def draw(self, screen):
        gfxdraw.filled_circle(screen, int(self.pos.x), int(self.pos.y), int(self.r), (255, 0, 0))
        gfxdraw.aacircle(screen, int(self.pos.x), int(self.pos.y), int(self.r), (0, 0, 0))

    def update(self, screen, player):
        self.move(player)
        self.draw(screen)
