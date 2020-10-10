import pygame


class Player:
    def __init__(self, x, y):
        self.pos = pygame.math.Vector2(x, y)
        self.v = 5
        self.R = 40

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos.y -= self.v
        if keys[pygame.K_s]:
            self.pos.y += self.v
        if keys[pygame.K_a]:
            self.pos.x -= self.v
        if keys[pygame.K_d]:
            self.pos.x += self.v

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 100, 100), (int(self.pos.x), int(self.pos.y)), self.R)

    def update(self, screen):
        self.move()
        self.draw(screen)



class Enemy:
    def __init__(self, x, y):
        self.pos = pygame.math.Vector2(x, y)
        self.R = 50
        self.v = 2

    def move(self, player):
        v = self.v * (player.pos - self.pos).normalize()
        self.pos += v

    def collision(self, player):
        if (self.pos - player.pos).magnitude() < self.R + player.R:
            print('Collision')

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.pos.x), int(self.pos.y)), self.R)

    def update(self, screen, player):
        self.move(player)
        self.collision(player)
        self.draw(screen)
