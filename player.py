import pygame
from pygame import gfxdraw

class Player:
    def __init__(self, x, y, v, r):
        self.pos = pygame.math.Vector2(x, y)
        self.dir = pygame.math.Vector2(0, 0)
        self.v = v
        self.r = r

    def move(self, screen):
        w, h = screen.get_size()
        keys = pygame.key.get_pressed()  # movement using WASD
        if keys[pygame.K_w]:
            self.dir.y = -1
        if keys[pygame.K_s]:
            self.dir.y = 1
        if keys[pygame.K_a]:
            self.dir.x = -1
        if keys[pygame.K_d]:
            self.dir.x = 1
        if self.dir.magnitude():
            self.dir = self.v * self.dir.normalize()
        self.pos += self.dir
        self.dir.update(0, 0)
        # making sure the player is within boundaries
        if self.pos.x > w - self.r:
            self.pos.x = w - self.r
        if self.pos.x < self.r:
            self.pos.x = self.r
        if self.pos.y > h - self.r:
            self.pos.y = h - self.r
        if self.pos.y < self.r:
            self.pos.y = self.r

    def draw(self, screen):
        gfxdraw.filled_circle(screen, int(self.pos.x), int(self.pos.y), int(self.r), (250, 200, 0))
        gfxdraw.aacircle(screen, int(self.pos.x), int(self.pos.y), int(self.r), (0, 0, 0))

    def update(self, screen):
        self.move(screen)
        self.draw(screen)
