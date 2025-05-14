import pygame

listOfKeys = []

def checkForKey(key):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == key or event.type == pygame.KEYUP and event.key == key:
            return True
        else:
            pass

def AddKey(key):
    listOfKeys.append(key)

