#!/usr/bin/env python2
import copy
import time
from random import randrange as rand
from field import Field
from ai import Ai
import pygame, sys

# The configuration
cell_size =    18
cols =        10
rows =        22
maxfps =     30
time =     25
maxPiece = 500

colors1 = [
(229,   31,   31  ),
(208, 0,   0  ),
(202,   137, 137 ),
(137,   24,   24),
(255, 154, 154  ),
(186, 49, 49  ),
(107, 0,   0),
(233,   76, 76),
(0,   0, 0)
]

colors2 = [
(61,   81,   145  ),
(175, 194,   255  ),
(8,   51, 193  ),
(49,   65,   118),
(57, 144, 243  ),
(0, 133, 210  ),
(182, 228,   255),
(30,   44, 134),
(0,   0, 0)
]

# Define the shapes of the single parts
tetris_shapes = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 0],
     [0, 3, 3]],

    [[4, 0, 0],
     [4, 4, 4]],

    [[0, 0, 5],
     [5, 5, 5]],

    [[6, 6, 6, 6]],

    [[7, 7],
     [7, 7]]
]

class Gui(object):
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(250,25)
        self.width = cell_size*(cols+6)
        self.height = cell_size*rows
        self.rlim = cell_size*cols
        self.bground_grid = [[ 8 if x%2==y%2 else 0 for x in range(cols)] for y in range(rows)]

        self.default_font =  pygame.font.Font(
            pygame.font.get_default_font(), 12)

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        pygame.time.set_timer(pygame.USEREVENT+1, time)

    def disp_msg(self, msg, topleft):
        x,y = topleft
        for line in msg.splitlines():
            self.screen.blit(
                self.default_font.render(
                    line,
                    False,
                    (255,255,255),
                    (0,0,0)),
                (x,y))
            y+=14

    def center_msg(self, msg):
        for i, line in enumerate(msg.splitlines()):
            msg_image =  self.default_font.render(line, False,
                (255,255,255), (0,0,0))

            msgim_center_x, msgim_center_y = msg_image.get_size()
            msgim_center_x //= 2
            msgim_center_y //= 2

            self.screen.blit(msg_image, (
              self.width // 2-msgim_center_x,
              self.height // 2-msgim_center_y+i*22))

    def draw_matrix(self, matrix, offset, player):
        off_x, off_y  = offset
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                if val:
                    if player == 1:
                        pygame.draw.rect(self.screen,colors1[val],
                            pygame.Rect(
                                (off_x+x) *
                                cell_size,
                                (off_y+y) *
                                cell_size,
                                cell_size,
                                cell_size),0)
                    else:
                        pygame.draw.rect(self.screen,colors2[val],
                            pygame.Rect(
                                (off_x+x) *
                                cell_size,
                                (off_y+y) *
                                cell_size,
                                cell_size,
                                cell_size),0)

    def update(self, tetris):
        self.screen.fill((0,0,0))
        if tetris.gameover:# or self.nbPiece >= maxPiece:
            self.center_msg("""Game Over!\nPlayer 1 Score: %d \nPlayer 2 Score: %dPress space to continue""" % tetris.score1, tetris.score2)
        else:
            if tetris.paused:
                self.center_msg("Paused")
            else:
                pygame.draw.line(self.screen,
                    (255,255,255),
                    (self.rlim+1, 0),
                    (self.rlim+1, self.height-1))
                self.disp_msg("Next:", (
                    self.rlim+cell_size,
                    2))
                self.disp_msg("P 1 Score: %d\n\nP2 Score: %d\n\nMoves Left: %d" % (tetris.score1, tetris.score2, tetris.moves_left),
                    (self.rlim+cell_size, cell_size*5))
                self.draw_matrix(self.bground_grid, (0,0), tetris.player)
                self.draw_matrix(tetris.board, (0,0), tetris.player)
                self.draw_matrix(tetris.stone, (tetris.stone_x, tetris.stone_y), tetris.player)
                self.draw_matrix(tetris.next_stone, (cols+1,2), tetris.player)
        pygame.display.update()
