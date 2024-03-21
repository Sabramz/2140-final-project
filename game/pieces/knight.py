from piece import Piece
import pygame
import os

class Knight(Piece):

    def __init__(self, x, y, team):
        super().__init__(x, y, team, "knight")
    
    # Each piece has a different set of possible moves.
    def possible_moves(self, board):
        x = self.x
        y = self.y
        moves = []
        '''
        x    p   x   p   x  
        p    x   x   x   p
        x    x   K   x   x
        p    x   x   x   p
        x    p   x   p   x
        if statements go clockwise
        '''
        if x + 1 <= 8 and y + 2 <= 8:
            moves.append((x+1,y+2))
        if x + 2 <= 8 and y + 1 <= 8:
            moves.append((x+2,y+1))
        if x + 2 <= 8 and 1 <= y - 1:
            moves.append((x+2,y-1))
        if x + 1 <= 8 and 1 <= y - 2:
            moves.append((x+1,y-2))
        if 1 <= x - 1 and 1 <= y - 2:
            moves.append((x+1,y+2))
        if 1 <= x - 2 and 1 <= y - 1:
            moves.append((x+1,y+2))
        if 1 <= x - 2 and y + 1 <= 8:
            moves.append((x+1,y+2))
        if 1 <= x - 1 and y + 2 <= 8:
            moves.append((x+1,y+2))
        return moves
    
    def to_image(self):
        file_name = ""
        if self.team == "White":
            file_name = "w_knight.png"
        else:
            file_name = "b_knight.png"
        return pygame.image.load(os.path.join('assets', file_name)).convert_alpha()
            
