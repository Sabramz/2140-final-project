import copy
from piece import Piece
import pygame
import os

class Knight(Piece):

    def __init__(self, team):
        super().__init__(team, "knight")
    
    # Each piece has a different set of possible moves.
    def possible_moves(self, board, pos, check_legal = True):
        x = pos[0]
        y = pos[1]
        moves = set()
        '''
        x    p   x   p   x  
        p    x   x   x   p
        x    x   K   x   x
        p    x   x   x   p
        x    p   x   p   x
        if statements go clockwise
        '''
        if x + 1 <= 8 and y + 2 <= 8 and board.moveable((x+1, y+2), self.team):
            moves.add((x+1,y+2))
        if x + 2 <= 8 and y + 1 <= 8 and board.moveable((x+2, y+1), self.team):
            moves.add((x+2,y+1))
        if x + 2 <= 8 and 1 <= y - 1 and board.moveable((x+2, y-1), self.team):
            moves.add((x+2,y-1))
        if x + 1 <= 8 and 1 <= y - 2 and board.moveable((x+1, y-2), self.team):
            moves.add((x+1,y-2))
        if 1 <= x - 1 and 1 <= y - 2 and board.moveable((x-1, y-2), self.team):
            moves.add((x-1,y-2))
        if 1 <= x - 2 and 1 <= y - 1 and board.moveable((x-2, y-1), self.team):
            moves.add((x-2,y-1))
        if 1 <= x - 2 and y + 1 <= 8 and board.moveable((x-2, y+1), self.team):
            moves.add((x-2,y+1))
        if 1 <= x - 1 and y + 2 <= 8 and board.moveable((x-1, y+2), self.team):
            moves.add((x-1,y+2))

        if check_legal:
            illegal_moves = set()
            for move in moves:
                new_board = copy.deepcopy(board)
                new_board.move_to(pos, move)
                if not new_board.is_legal(self.team):
                    illegal_moves.add(move)
            moves = moves.symmetric_difference(illegal_moves)
            
        return moves
    
    def to_image(self):
        file_name = ""
        if self.team == "White":
            file_name = "w_knight.png"
        else:
            file_name = "b_knight.png"
        return pygame.image.load(os.path.join('assets', file_name)).convert_alpha()
            
