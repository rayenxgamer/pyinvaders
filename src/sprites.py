import pygame

class Sprites:
    def __init__(self,screen, texture, x, y, w, h):
        self.texture = texture
        self.texture = pygame.transform.scale(self.texture, (h,w))
        self.x = x
        self.initialPos = self.x
        self.y = y
        self.w = w
        self.h = h
        self.screen = screen
        #self.left = False
        #self.right = False
        #self.up = False
        #self.down = False

    def draw(self):
        self.screen.blit(self.texture, (self.x, self.y))

    def setPos(self, x, y):
        self.x = x
        self.y = y
