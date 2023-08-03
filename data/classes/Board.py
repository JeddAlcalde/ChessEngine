# Jedd Alcalde

import pygame
from Square import Square
from pieces.Rook import Rook
from pieces.Bishop import Bishop
from pieces.Knight import Knight
from pieces.King import King
from pieces.Pawn import Pawn
from pieces import Queen
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tile_width = width // 8
        self.tile_height = height // 8
        self.selected_piece = None
        self.turn = 'white'
        self.config = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        self.squares = self.generate_squares()
        self.setup_board()

    def generate_squares(self):
        output = []
        for y in range(8):
            for x in range(8):
                output.append(Square(x,  y, self.tile_width, self.tile_height))
        return output
        
    def get_square_from_pos(self, pos):
        for square in self.squares:
            if (square.x, square.y) == (pos[0], pos[1]):
                return square
            
    def get_piece_from_pos(self, pos):
        return self.get_square_from_pos(pos).occupying_piece
    
    def setup_board(self):
        for y, row in enumerate(self.config):
            for x, piece in enumerate(row):
                if piece != '':
                    square = self.get_square_from_pos((x,y,))
                    #looking inside contents, what piece does it have
                    if piece[1] == 'R':
                        square.occupying_piece = Rook((x,y), 'white' if piece[0] == 'w' else 'black', self)
                    elif piece[1] == 'N':
                        square.occupying_piece = Knight((x,y), 'white' if piece[0] == 'w' else 'black', self)
                    elif piece[1] == 'B':
                        square.occupying_piece = Bishop((x,y), 'white' if piece[0] == 'w' else 'black', self)
                    elif piece[1] == 'Q':
                        square.occupying_piece = Queen((x,y), 'white' if piece[0] == 'w' else 'black', self)
                    elif piece[1] == 'K':
                        square.occupying_piece = King((x,y), 'white' if piece[0] == 'w' else 'black', self)
                    elif piece[1] == 'Pawn':
                        square.occupying_piece = Pawn((x,y), 'white' if piece[0] == 'w' else 'black', self)

    def handle_click(self, mx, my):
        x = mx // self.width
        y = my //self.height
        clicked_square = self.get_square_from_pos
        #to select a piece
        if (self.selected_piece == None) & (clicked_square.occupying_piece != None) & (clicked_square.occupying_piece.color == self.turn):
            self.selected_piece = clicked_square.occupying_piece
        #move a selected piece to an empty clicked square if legal
        elif self.selected_piece.move(self, clicked_square):
            self.turn = 'white' if self.turn == 'black' else 'black'
        #to select a new piece
        elif (clicked_square.occupying_piece != None) & (clicked_square.occupying_piece.color == self.turn):
            self.selected_piece = clicked_square.occupying_piece

    def is_in_checkmate(self, color):
        for piece in [i.occupying_piece for i in self.squares]:
            if (piece != None) & (piece.notation == 'K') & (piece.color == color):
                king = piece
            if (king.get_valid_moves(self) == []) & (self.is_in_check(color)):
                return True
        return False

    def draw(self, display):
        if self.selected_piece is not None:
            self.get_square_from_pos(self.selected_piece.pos).highlight = True
            for square in self.selected_piece.get_valid_moves(self):
                square.highlight = True
        for square in self.squares:
            square.draw(display)