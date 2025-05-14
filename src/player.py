from src.sprites import*

class player(Sprites):
    def __init__(self,screen, texture, x, y, w, h, health):
        self.texture = texture
        self.texture = pygame.transform.scale(self.texture, (h,w))
        self.x = x
        self.initialPos = self.x
        self.y = y
        self.w = w
        self.h = h
        self.screen = screen
        self.health = health

    def setHealth(self, health):
        self.health = health

    def updateDeathState(self):
        if self.health == 0:
            self.dead = True
        else:
            self.dead = False
