# Jedd Alcalde

import pygame
from data.classes.Board import Board

pygame.init()

WINDOW_SIZE = (600,600)

screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

piece_values = {
    "pawn" : 100,
    "rook" : 500,
    "bishop" : 330,
    "knight" : 320,
    "queen" : 900,
    "king" : 2000
}

def draw(display):
    display.fill('white')
    board.draw(display)
    pygame.display.update()

if __name__ == '__main__':
    running = True
    print("Game Started")
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
        # Quit the game if the user presses the close button
            if event.type == pygame.QUIT:
                print("Game Ended")
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
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