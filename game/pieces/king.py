from piece import Piece
import pygame
import os

class King(Piece):

    def __init__(self, team):
        super().__init__(team, "king")
    
    # Each piece has a different set of possible moves.
    def possible_moves(self, board, pos):
        x = pos[0]
        y = pos[1]
        moves = set()
       
       # TODO: Make sure x and y are in bounds
        if y + 1 < 8:
            if board.open_square(x,y):
                moves.add((x, y + 1))
        if y - 1 > 1:
            if board.open_square(x,y):
                moves.add((x, y - 1))
        if x + 1 < 8:
            if board.open_square(x,y):
                moves.add((x + 1, y))
        if 1 < x - 1:
            if board.open_square(x,y):
                moves.add((x - 1, y))

        if y + 1 < 8 and x + 1 < 8:
            if board.open_square(x,y):
                moves.add((x + 1, y + 1))
        if y - 1 > 1 and x + 1 < 8:
            if board.open_square(x,y):
                moves.add((x + 1, y - 1))
        if x - 1 < 8 and y - 1 > 1:
            if board.open_square(x,y):
                moves.add((x - 1, y - 1))
        if 1 < x - 1 and y + 1 < 8:
            if board.open_square(x,y):
                moves.add((x - 1, y + 1))

        other_team_moves = set()
        if self.team == "White":
            pass
            other_team_moves = board.team_possible_moves("Black")
        else:
            pass
            other_team_moves = board.team_possible_moves("White")
        
        impossible_moves = set()
        for move in moves:
            if move in other_team_moves:
                impossible_moves.add(move)
        
        return moves.symmetric_difference(impossible_moves)
        
    


    # override
    def is_king(self):
        return True

    def to_image(self):
        file_name = ""
        if self.team == "White":
            file_name = "w_king.png"
        else:
            file_name = "b_king.png"
        return pygame.image.load(os.path.join('assets', file_name)).convert_alpha()