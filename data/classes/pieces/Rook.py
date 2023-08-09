# Jedd Alcalde

import pygame
import sys
sys.path.append('data/classes/pieces/Piece.py')

def Rook(Piece):
    def __init__(self, pos, color, board):
        super.__init__(pos, color, board)
        img_path = 'data/imgs/' + color[0] + '_rook.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))
        self.notation = 'R'

    def get_possible_moves(self, board):
        output = []
        moves_north = []
        for y in range(self.y)[::-1]:
            moves_north.append(board.get_square_from_pos(self.x, y))
        moves_east = []
        for x in range(self.x + 1, 8):
            moves_east.append(board.get_square_from_pos(x, self.y))
        moves_south = []
        for y in range(self.y + 1, 8):
            moves_south.append(board.get_square_from_pos(self.x, y))
        moves_west = []
        for y in range(self.x)[::-1]:
            moves_west.append(board.get_square_from_pos(x, self.y))
        output.append(moves_north)
        output.append(moves_east)
        output.append(moves_south)
        output.append(moves_west)
        return output