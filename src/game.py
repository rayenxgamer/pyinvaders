import pygame
from src.renderer import*
from src.enemySpawner import*
from src.enemyBullet import*
from src.enemy import*
from src.collision import*
from src.bullet import*
from src.colors import*
from src.text import*
from src.sprites import*
from src.player import*


SPEED = 68


class game:
    def __init__(self, title, h, w):
        self.title = title
        self.h = h
        self.w = w

    def startGame(self):
        self.running = True

        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption(self.title)

        self.level = 0

        self.LevelTutorial = enemySpawner("assets/levels/levelTutorial.txt", self.screen)
        self.LevelTutorial.initSpawnFile()

        self.Level1 = enemySpawner("assets/levels/level1.txt", self.screen)
        self.Level1.initSpawnFile()

        self.Level2 = enemySpawner("assets/levels/level2.txt", self.screen)
        self.Level2.initSpawnFile()

        self.Level3 = enemySpawner("assets/levels/level3.txt", self.screen)
        self.Level3.initSpawnFile()

        self.Level4 = enemySpawner("assets/levels/level4.txt", self.screen)
        self.Level4.initSpawnFile()

        self.Level5 = enemySpawner("assets/levels/level5.txt", self.screen)
        self.Level5.initSpawnFile()

        self.Level99 = enemySpawner("assets/levels/level99.txt", self.screen)
        self.Level99.initSpawnFile()

        PLAYER_X = 350
        PLAYER_Y = 400

        self.playerAbleToShoot = True
        self.EnemiesAbleToShoot = True

        self.grass = player(self.screen,pygame.image.load("assets/ship.png"),PLAYER_X,PLAYER_Y , 68, 68, 200)
        self.bullets = []
        self.enemyBullets = []

        self.levelInfoHud = Text("monospace", "1", 680, 450, 150, WHITE, BLACK)
        self.levelRestartInfo = Text("monospace", "you died! press R to restart", 680, 450, 15, WHITE, BLACK)
        self.gameBeginInfo = Text("monospace", "press space to start", 680, 450, 15, WHITE, BLACK)
        self.playerInfoHud = Text("monospace", "health: " + str(int(self.grass.health)), 100, 900, 12, WHITE, BLACK)

        self.startGameLoop()

    def startGameLoop(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            self.checkWinCondition()

            self.playerInfoHud.draw(self.screen)
            if self.grass.health > 0:
                self.levelInfoHud.draw(self.screen)

            self.grass.draw()
            self.playerInfoHud.text = "health: " + str(int(self.grass.health))

            for bullet in self.bullets:
                bullet.y -= 2
                bullet.fireBullet(self.screen, 10);
                if bullet.y == 0:
                    self.bullets.remove(bullet)

            if len(self.enemyBullets) < 5:
                if self.EnemiesAbleToShoot:
                    for bulletE in self.enemyBullets:
                        bulletE.y += 0.25
                        bulletE.fireBullet(self.screen, 10);
                        if bulletE.y == self.h:
                            self.enemyBullets.remove(bulletE)

            if self.grass.health > 0:
                if self.level == 0:
                    self.playerAbleToShoot = False
                    self.EnemiesAbleToShoot = False
                    self.LevelTutorial.drawEnemies(self.bullets, self.enemyBullets, self.grass)
                    self.levelInfoHud.text = ""
                    self.gameBeginInfo.draw(self.screen)
                if self.level == 1:
                    self.Level1.drawEnemies(self.bullets, self.enemyBullets, self.grass)
                    self.levelInfoHud.text = "1"
                if self.level == 2:
                    self.Level2.drawEnemies(self.bullets, self.enemyBullets, self.grass)
                    self.levelInfoHud.text = "2"
                if self.level == 3:
                    self.Level3.drawEnemies(self.bullets, self.enemyBullets, self.grass)
                    self.levelInfoHud.text = "3"
                if self.level == 4:
                    self.Level4.drawEnemies(self.bullets, self.enemyBullets, self.grass)
                    self.levelInfoHud.text = "4"
                if self.level == 5:
                    self.Level5.drawEnemies(self.bullets, self.enemyBullets, self.grass)
                    self.levelInfoHud.text = "5"
                if self.level == 99:
                    self.playerAbleToShoot = False
                    self.EnemiesAbleToShoot = False
                    self.grass.x = self.w // 2.25
                    self.grass.y = self.h // 2.25
                    self.Level99.drawEnemies(self.bullets, self.enemyBullets, self.grass)
                    self.levelInfoHud.text = "end?"
            else:
                self.levelRestartInfo.draw(self.screen)
                print("dead")


            self.limitPlayerToScreen()
            self.processInput()
            pygame.display.update()
            pygame.display.flip()

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    self.running = False
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.grass.x -= SPEED
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.grass.x += SPEED
                elif event.key == pygame.K_r:
                    self.grass.health = 200
                    self.Level1.initSpawnFile()
                    self.enemyBullets.clear()
                    self.level = 1
                elif event.key == pygame.K_SPACE:
                    if (self.playerAbleToShoot):
                        if len(self.bullets) < 4:
                            pygame.mixer.music.load("assets/music/shoot.wav");
                            pygame.mixer.music.play(0)
                            self.bullets.append(Bullet(self.grass))
                    elif not self.playerAbleToShoot and self.level == 0:
                        self.level = 1
                        self.playerAbleToShoot = True
                        self.EnemiesAbleToShoot = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (self.playerAbleToShoot):
                    if len(self.bullets) < 4:
                        pygame.mixer.music.load("assets/music/shoot.wav");
                        pygame.mixer.music.play(0)
                        self.bullets.append(Bullet(self.grass))
                elif not self.playerAbleToShoot and self.level == 0:
                    self.level = 1
                    self.playerAbleToShoot = True
                    self.EnemiesAbleToShoot = True


    def checkWinCondition(self):
        if not self.Level1.enemyList and self.level == 1:
            pygame.mixer.music.load("assets/music/win.wav")
            pygame.mixer.music.play(0)
            self.enemyBullets.clear()
            self.grass.x = self.grass.initialPos
            self.grass.health = 200
            self.level = 2
        elif not self.Level2.enemyList and self.level == 2:
            pygame.mixer.music.load("assets/music/win.wav")
            pygame.mixer.music.play(0)
            self.enemyBullets.clear()
            self.grass.health = 200
            self.grass.x = self.grass.initialPos
            self.level = 3
        elif not self.Level3.enemyList and self.level == 3:
            pygame.mixer.music.load("assets/music/win.wav")
            pygame.mixer.music.play(0)
            self.enemyBullets.clear()
            self.grass.health = 200
            self.grass.x = self.grass.initialPos
            self.level = 4
        elif not self.Level4.enemyList and self.level == 4:
            pygame.mixer.music.load("assets/music/win.wav")
            pygame.mixer.music.play(0)
            self.enemyBullets.clear()
            self.grass.health = 200
            self.grass.x = self.grass.initialPos
            self.level = 5
        elif not self.Level5.enemyList and self.level == 5:
            pygame.mixer.music.load("assets/music/win.wav")
            pygame.mixer.music.play(0)
            self.enemyBullets.clear()
            self.grass.health = 200
            self.grass.x = self.w // 2.25
            self.grass.y = self.h // 2
            self.level = 99
        else:
            pass
    def limitPlayerToScreen(self):
        if self.grass.x <= 0:
            self.grass.x = 10

        if self.grass.x >= 622:
            self.grass.x = 622



