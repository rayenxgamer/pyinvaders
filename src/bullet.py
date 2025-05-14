import pygame
from src.player import*

class Bullet:
    def __init__(self, player):
        self.x = player.x + 18
        self.y = player.y + 10
        self.h = 50
        self.w = 25

    def fireBullet(self,screen, dir):
        self.bullet = Sprites(screen,pygame.image.load("assets/bullet.png"),self.x,self.y , self.h, self.w)
        self.bullet.draw()

