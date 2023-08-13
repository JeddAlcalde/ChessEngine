#Jedd Alcalde

import pygame
import sys
sys.path.append('data/classes/Board.py')
import Board

pygame.init()

WINDOW_SIZE = (600,600)

screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

def draw(display):
    display.fill('white')
    board.draw(display)
    pygame.display.update()

if __name__ == '__main__':
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
        # Quit the game if the user presses the close button
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONGDOWN:
                # If Mouse is clicked
                if event.button == 1:
                    board.handle_click(mx, my)
        if board.is_in_checkmate('black'): # black is in checkmate
            print('White wins!')
            running = False
        elif board.is_in_checkmate('white'): # white is in checkmate
            print('Black wins!')
            running = False
        #Draw the board
        draw(screen)