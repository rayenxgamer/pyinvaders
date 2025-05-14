from src.sprites import*
from src.enemyBullet import*

class Enemy(Sprites):
    def __init__(self,screen, texture, x, y, w, h, initialHealth):
        self.screen = screen
        self.texture = texture
        self.texture = pygame.transform.scale(self.texture, (h,w))
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.initialHealth = initialHealth

    def dropHealthBy(self,damage):
        self.initialHealth -= damage

