from piece import Piece
import pygame
import os

class King(Piece):

    def __init__(self, x, y, team):
        super().__init__(x, y, team, "king")
    
    # Each piece has a different set of possible moves.
    def possible_moves(self, board):
        x = self.x
        y = self.y
       
        possible_moves = set([ (x-1,y+1), (x, y+1), (x+1,y+1), (x-1,y), (x+1,y), (x-1,y-1), (x, y-1), (x+1,y-1) ])
        other_team_moves = set()
        if self.team == "White":
            other_team_moves = board.team_possible_moves("Black")
        else:
            other_team_moves = board.team_possible_moves("White")
        
        impossible_moves = set()
        for move in possible_moves:
            if move in other_team_moves:
                impossible_moves.add(move)
        
        return possible_moves.symmetric_difference(impossible_moves)
                


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