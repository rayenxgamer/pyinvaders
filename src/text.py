import pygame
from src.sprites import*

class Text:
    def __init__(self,fontname, text, x, y, size, textColor, backgroundColor):
        self.fontname = fontname
        self.text = str(text)
        self.x = int(x)
        self.y = int(y)
        self.size = int(size)
        self.textColor = textColor
        self.backgroundColor = backgroundColor
        self.font = pygame.font.SysFont(self.fontname, self.size, pygame.font.Font.bold)


    def draw(self, screen):
        self.TextToRender = self.font.render(self.text, True, self.textColor, self.backgroundColor)
        self.TextureRectSurface = self.TextToRender.get_rect()
        self.TextureRectSurface.center = (self.x // 2, self.y // 2)
        screen.blit(self.TextToRender, self.TextureRectSurface)
