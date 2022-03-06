import pygame
import sys
import asyncio
import time
from config import *
from computer_player import *
from draw import *

pygame.init()

screen = draw_screen()

board = new_board()

pygame.display.update()

game_over = False

while True:
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if game_over:
               pygame.quit()
            pos = pygame.mouse.get_pos()
            x = pos[0] // 40
            y = pos[1] // 40
            drawX(screen, x, y)
            board[x][y] = 1
            if check_if_end_game(screen, board):
                pygame.display.update()
                ev1 = pygame.event.get()
                game_over = True
                continue

            pygame.display.update()
            computer_reply(screen, board)
            if check_if_end_game(screen, board):
                pygame.display.update()
                ev = pygame.event.get()
                game_over = True
                continue

            pygame.display.update()
    # next_turn = True