import pygame
from random import randint
from dungeon import Dungeon_room
from player import Player

pygame.init()

# окно
win_width = 1920
win_height = 1080

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('#')

FPS = 120
clock = pygame.time.Clock()

hero = Player()

out_from = 'l'

# перенести на переход персонажа
next_room = randint(0, 6)
# перенести на переход персонажа

player_equipment = ['base-armor', 'base-sword']

def dungeon():
    global player_equipment
    room = Dungeon_room(win_width, win_height)
    room.blit_new_room(out_from, win, next_room)
    hero.blit(win)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    dungeon()

    clock.tick(FPS)
    pygame.display.flip()
