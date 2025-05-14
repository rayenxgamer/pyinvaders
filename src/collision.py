from src.enemy import*
from src.enemySpawner import*
from src.sprites import*
from src.bullet import*
import pygame

def checkforCollision(bullet, enemy):
    if bullet.x + bullet.w >= enemy.x and enemy.x + enemy.h >= bullet.x and bullet.y + bullet.h >= enemy.y and enemy.y + enemy.w >= bullet.y:
            return True
    return False
