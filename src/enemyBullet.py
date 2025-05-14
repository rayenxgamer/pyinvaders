from src.bullet import*
import pygame

class enemyBullet(Bullet):

    def __init__(self, player):
        self.x = player.x + 15
        self.y = player.y - 10
        self.h = 50
        self.w = 25

    def fireBullet(self,screen, dir):
        self.bullet = Sprites(screen,pygame.image.load("assets/enemyBullet.png"),self.x,self.y , self.h, self.w)
        self.bullet.draw()
