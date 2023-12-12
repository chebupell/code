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
        self.inDungeon_img = pygame.transform.scale(pygame.image.load('img/mini_main-char.png'), (self.width, self.height))
        self.inDungeon_run = []
        for i in range(7):
            self.inDungeon_run.append(pygame.transform.scale(pygame.image.load('animations/mini_main-char/sprite_'+str(i)+'.png'), (self.width, self.height)))
        self.rect = self.inDungeon_img.get_rect()

    def draw(self, win):
        win.blit(self.inDungeon_img, (self.x, self.y))

    def blit(self, win):
        self.velX = 0
        self.velY = 0
        if pygame.mouse.get_pressed()[0]:
            self.attack = True

        if not self.attack:
            self.speed = 4
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.run_l = True
            if keys[pygame.K_w]:
                self.run_t = True
            if keys[pygame.K_s]:
                self.run_b = True
            if keys[pygame.K_d]:
                self.run_r = True
            if self.run_l and not self.run_r:
                if self.animCount > 6:
                    self.animCount = 0
                self.velX = -self.speed
                win.blit(self.inDungeon_run[self.animCount], (self.x, self.y))
                self.animCount += 1
            if self.run_t and not self.run_b:
                if self.animCount > 6:
                    self.animCount = 0
                self.velY = -self.speed
                win.blit(self.inDungeon_run[self.animCount], (self.x, self.y))
                self.animCount += 1
            if self.run_b and not self.run_t:
                if self.animCount > 6:
                    self.animCount = 0
                self.velY = self.speed
                win.blit(self.inDungeon_run[self.animCount], (self.x, self.y))
                self.animCount += 1
            if self.run_r and not self.run_l:
                if self.animCount > 6:
                    self.animCount = 0
                self.velX = self.speed
                win.blit(self.inDungeon_run[self.animCount], (self.x, self.y))
                self.animCount += 1
            else:
                win.blit(self.inDungeon_img, (self.x, self.y))
            self.run_l = False
            self.run_b = False
            self.run_t = False
            self.run_r = False
            self.x += self.velX
            self.y += self.velY