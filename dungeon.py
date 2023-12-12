import pygame

class Dungeon_room():
    def __init__(self, win_width, win_height):
        self.from_l = [pygame.transform.scale(pygame.image.load('dungeon/rooms/room-l.png'), (win_width, win_height)),
                       pygame.transform.scale(pygame.image.load('dungeon/rooms/room_l-b.png'), (win_width,
                                                                                                 win_height)),
                       pygame.transform.scale(pygame.image.load('dungeon/rooms/room_l-t.png'), (win_width,
                                                                                                 win_height)),
                       pygame.transform.scale(pygame.image.load('dungeon/rooms/room_AllExcB.png'), (win_width,
                                                                                                     win_height)),
                       pygame.transform.scale(pygame.image.load('dungeon/rooms/room_AllExcR.png'), (win_width,
                                                                                                     win_height)),
                       pygame.transform.scale(pygame.image.load('dungeon/rooms/room_AllExcT.png'), (win_width,
                                                                                                     win_height)),
                       pygame.transform.scale(pygame.image.load('dungeon/rooms/room_r-l.png'), (win_width, win_height))]

    def blit_new_room(self, out_from, win, next_room):
        if out_from == 'l':
            win.blit(self.from_l[next_room], (0, 0))

