from enemy import Enemy
from player import Player
import pygame
import math


class Game:
    def __init__(self, w, h):
        # main initialize
        pygame.init()
        self.w, self.h = w, h
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption('A simple game')
        self.clock = pygame.time.Clock()

        # all the text stuff
        self.menuFont = pygame.font.SysFont('None', 70)
        self.inGameFont = pygame.font.SysFont('None', 35)
        self.scoreText = self.menuFont.render("You haven't played yet", 1, (0, 0, 0))
        self.playText = self.menuFont.render('Start', 1, (0, 0, 0))
        self.quitText = self.menuFont.render('Quit', 1, (0, 0, 0))
        self.levelNumber = self.inGameFont.render('Level %i' % 1, 1, (0, 0, 0))
        self.levelHighScore = self.inGameFont.render('High score: %i' % 0, 1, (0, 0, 0))
        self.playButton = pygame.Surface((self.w * 2 / 7, self.h * 9 / 70))
        self.quitButton = pygame.Surface((self.w * 2 / 7, self.h * 9 / 70))
        self.g = self.r = 100
        self.playButton.fill((0, self.g, 0))
        self.playButton.blit(self.playText, (self.w / 7 - self.playText.get_size()[0] / 2, self.h * 9 / 120 - 25))
        self.quitButton.fill((self.r, 0, 0))
        self.quitButton.blit(self.quitText, (self.w / 7 - self.quitText.get_size()[0] / 2, self.h * 9 / 140 - 25))

        # game preparation
        self.score = 0
        self.level = 1
        self.p = Player(w - min(w, h) / 20, h - 40 - min(w, h) / 20, min(w, h) / 120, min(w, h) / 20)
        self.e = []
        self.R = pygame.math.Vector2(2.2 * self.p.r, 2.2 * self.p.r)
        self.playing = False
        self.onLevel = False
        self.running = True

    def run(self):
        while self.running:
            if self.playing:
                self.play()
            else:
                self.menu()

            pygame.display.update()
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def menu(self):
        # filling buttons buttons
        self.playButton.fill((0, self.g, 0))
        self.playButton.blit(self.playText, (self.w / 7 - self.playText.get_size()[0] / 2, self.h * 9 / 120 - 25))
        self.quitButton.fill((self.r, 0, 0))
        self.quitButton.blit(self.quitText, (self.w / 7 - self.quitText.get_size()[0] / 2, self.h * 9 / 140 - 25))
        # drawing the main menu
        self.screen.fill((200, 200, 200))
        self.screen.blit(self.scoreText, (self.w / 2 - self.scoreText.get_size()[0] / 2, self.h * 2 / 7))
        self.screen.blit(self.playButton, (self.w * 5 / 14, self.h * 19 / 35))
        self.screen.blit(self.quitButton, (self.w * 5 / 14, self.h * 24 / 35))
        self.g = self.r = 100
        x, y = pygame.mouse.get_pos()
        if self.w * 5 / 14 < x < self.w * 9 / 14:  # checking for button interaction
            if self.h * 19 / 35 < y < self.h * 47 / 70:
                self.g = 150
                if pygame.mouse.get_pressed()[0]:
                    self.playing = True
            if self.h * 24 / 35 < y < self.h * 57 / 70:
                self.r = 150
                if pygame.mouse.get_pressed()[0]:
                    self.running = False

    def play(self):
        self.generate()
        while self.onLevel:
            self.screen.fill((240, 240, 240))
            self.screen.blit(self.levelNumber, (self.w - 1 - self.levelNumber.get_size()[0], 0))
            self.screen.blit(self.levelHighScore, (self.w - 1 - self.levelHighScore.get_size()[0], 20))
            pygame.draw.rect(self.screen, (0, 100, 0), (0, 0, int(self.R.x), int(self.R.y)))
            pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, int(self.R.x), int(self.R.y)), 2)
            self.p.update(self.screen)
            for enemy in self.e:
                enemy.update(self.screen, self.p)
                if enemy.collision(self.p):
                    self.onLevel = False
                    self.playing = False
                    self.level = 1
                    self.scoreText = self.menuFont.render('High score: %i' % self.score, 1, (0, 0, 0))
            pygame.display.update()

            if self.p.pos.x < self.R.x + self.p.r and self.p.pos.y < self.R.y + self.p.r:
                if self.p.pos.magnitude() < self.p.r * (math.sqrt(2) * 2.2 + 1):
                    if self.level > self.score:
                        self.score = self.level
                        self.levelHighScore = self.inGameFont.render('High score: %i' % self.score, 1, (0, 0, 0))
                    self.level += 1
                    self.onLevel = False

            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.onLevel = False
                    self.running = False

    def generate(self):
        self.p.pos.update(self.w - self.p.r, self.h - self.p.r)
        self.onLevel = True
        self.levelNumber = self.inGameFont.render('Level %i' % self.level, 1, (0, 0, 0))
        self.e = []
        for i in range(self.level):
            self.e.append(
                Enemy((2 * i + 1) * 0.3 * self.w / self.level, self.h * 0.3 + self.h * 0.3 * math.sin(i),
                      self.p.v * 0.3,
                      self.p.r))
