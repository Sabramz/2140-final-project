from piece import Piece
import pygame
import os

class Pawn(Piece):

    def __init__(self, x, y, team):
        super().__init__(x, y, team, "pawn")
        # If a pawn has not moved, it may advance one square instead of two
        self.moved = False

    # Check if there is an empty square infront of the pawn, or if there is a piece 1 square
    # diagonal and infront of the pawn
    '''
    Possible moves for the pawn
    x   o   x
    p   o   p
    x   P  x
    x   x   x
    '''
    def possible_moves(self, board):
        if self.team == "White":
            return self.possible_moves_white(board)
        else:
            return self.possible_moves_black(board)
    
    def possible_moves_white(self, board):
        moves = []
        x = self.x
        y = self.y
        if board.open_square(x, y + 1):
            moves.append((x, y+1))
        if not self.moved and board.open_square(x, y + 2):
            moves.append((x, y+2))
        if not board.open_square(x - 1, y + 1):
            moves.append((x-1, y+1))
        if not board.open_square(x + 1, y + 1):
            moves.append((x+1, y+1))
        return moves

    def possible_moves_white(self, board):
        moves = []
        x = self.x
        y = self.y
        if board.open_square(x, y - 1):
            moves.append((x, y-1))
        if not self.moved and board.open_square(x, y - 2):
            moves.append((x, y-2))
        if not board.open_square(x - 1, y - 1):
            moves.append((x-1, y-1))
        if not board.open_square(x + 1, y - 1):
            moves.append((x+1, y-1))
        return moves

    def to_image(self):
        file_name = ""
        if self.team == "White":
            file_name = "w_pawn.png"
        else:
            file_name = "b_pawn.png"
        return pygame.image.load(os.path.join('assets', file_name)).convert_alpha()
