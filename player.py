import pygame

class Player():
    def __init__(self):
        self.x = 400
        self.y = 500
        self.height = 150
        self.width = 175
        self.speed = 15
        self.damage = 1
        self.animCount = 0
        self.attack = False
        self.run_l = False
        self.run_b = False
        self.run_t = False
        self.run_r = False
        self.velX = 0
        self.velY = 0
        self.inDungeon_img = pygame.transform.scale(pygame.image.load('img/mini_main-char.png'), (self.width, self.height))
        self.inDungeon_run = []
        for i in range(8):
            self.inDungeon_run.append(pygame.transform.scale(pygame.image.load('animations/mini_main-char/sprite_'+str(i)+'.png'), (self.width, self.height)))
        self.rect = self.inDungeon_img.get_rect()

    def draw(self, win):
        win.blit(self.inDungeon_img, (self.x, self.y))

    def blit(self, win):
        self.velX = 0
        self.velY = 0
        if pygame.mouse.get_pressed()[0]:
            self.attack = True

        self.speed = 20
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.run_l = True
        else:
            self.run_l = False
        if keys[pygame.K_w]:
            self.run_t = True
        else:
            self.run_t = False
        if keys[pygame.K_s]:
            self.run_b = True
        else:
            self.run_b = False
        if keys[pygame.K_d]:
            self.run_r = True
        else:
            self.run_r = False
        if self.run_l or self.run_r:
            if self.animCount > 6:
                self.animCount = 0
            if self.run_l:
                if self.x >= -50:
                    self.x -= self.speed
                win.blit(self.inDungeon_run[self.animCount], (self.x, self.y))
                pygame.time.wait(50)
                self.animCount += 1
            elif self.run_r:
                if self.x <= 1450:
                    self.x += self.speed
                win.blit(self.inDungeon_run[self.animCount], (self.x, self.y))
                pygame.time.wait(50)
                self.animCount += 1
        elif self.run_t or self.run_b:
            if self.animCount > 6:
                self.animCount = 0
            if self.run_t:
                if self.y >= -50:
                    self.y -= self.speed
                win.blit(self.inDungeon_run[self.animCount], (self.x, self.y))
                pygame.time.wait(50)
                self.animCount += 1
            elif self.run_b:
                if self.y <= 500:
                    self.y += self.speed
                win.blit(self.inDungeon_run[self.animCount], (self.x, self.y))
                pygame.time.wait(50)
                self.animCount += 1

        else:
            win.blit(self.inDungeon_img, (self.x, self.y))
        self.x += self.velX
        self.y += self.velY
