from src.enemy import*
from src.enemyBullet import*
from src.sprites import*
from src.collision import*
from src.game import*
import random
import pygame

class enemySpawner:
    def __init__(self,filePath, screen):
        self.filePath = filePath
        self.screen = screen
        self.enemyList = []

    def initSpawnFile(self):
        self.file = open(self.filePath, 'r')
        for line in self.file:
            if line[0] == 'p':
                start = line.find("pos") + 5
                finish = line.find(",")
                self.EnemyXpos = int(line[start:finish].split()[0])
                self.EnemyYpos = int(line[start:finish].split()[1])
                print("x pos is", self.EnemyXpos)
                print("y pos is", self.EnemyYpos)
            if line[line.find(",") + 2] == 't':
                start = line.find("texture") + 11
                end = line.find(",",start) - 1
                self.TexturePath = str(line[start:end])
            if line.find("health") != -1:
                start = line.find("health") + 8
                end = len(line)
                self.healthValue = int(line[start:end])
                print("the enemy health is", self.healthValue)

            self.enemyList.append(Enemy(self.screen,pygame.image.load(self.TexturePath), self.EnemyXpos, self.EnemyYpos, 50, 50, self.healthValue))

        self.file.close()

    def drawEnemies (self, bullets, enemyBulletList, player):
        self.updateEnemiesAttackState(enemyBulletList, player)
        for enemy in self.enemyList:
            enemy.draw()
            for bullet in bullets:
                if (checkforCollision(bullet, enemy)):
                    if bullet.y == enemy.y:
                        bullets.remove(bullet)

                    enemy.initialHealth -= 5
                    if enemy.initialHealth <= 0:
                        pygame.mixer.music.load("assets/music/Enemydeath.wav")
                        pygame.mixer.music.play(0)
                        self.enemyList.remove(enemy)

    def updateEnemiesAttackState(self, enemyBulletList, player):
        selected_enemy = random.choice(self.enemyList)
        if len(enemyBulletList) < 3:
            enemyBulletList.append(enemyBullet(selected_enemy))
        for Ebullet in enemyBulletList:
            if (checkforCollision(Ebullet, player)):

                if Ebullet.y + player.h + Ebullet.h == player.y + player.h + Ebullet.h:
                    enemyBulletList.remove(Ebullet)
                    print("removed bullet");

                if player.health > 0:
                    player.health -= 0.10
                else:
                    pygame.mixer.music.load("assets/music/death.wav")
                    pygame.mixer.music.play(0)
                    player.health = 0

