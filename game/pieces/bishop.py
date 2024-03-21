from piece import Piece
import pygame
import os

class Bishop(Piece):

    def __init__(self, x, y, team):
        super().__init__(x, y, team, "bishop")
    
    # Each piece has a different set of possible moves.
    def possible_moves(self, board):
        moves = []
        x = self.x
        y = self.y
        # up right
        while 1 <= x and x <= 8 or 1 <= y and y <= 8:
            x += 1
            y += 1
            moves.append((x,y))
            # If there is a piece in the way, it can be taken, but this Bishop cannot move past it
            if not board.open_square(x,y):
                break
        x = self.x
        y = self.y
        # down right
        while 1 <= x and x <= 8 or 1 <= y and y <= 8:
            x += 1
            y -= 1
            moves.append((x,y))
            if not board.open_square(x,y):
                break
        x = self.x
        y = self.y
        # down left
        while 1 <= x and x <= 8 or 1 <= y and y <= 8:
            x -= 1
            y -= 1
            moves.append((x,y))
            if not board.open_square(x,y):
                break
        x = self.x
        y = self.y
        # up left
        while 1 <= x and x <= 8 or 1 <= y and y <= 8:
            x -= 1
            y += 1
            moves.append((x,y))
            if not board.open_square(x,y):
                break
        return moves

    def possible_moves(self, board):
        pass

    def to_image(self):
        file_name = ""
        if self.team == "White":
            file_name = "w_bishop.png"
        else:
            file_name = "b_bishop.png"
        return pygame.image.load(os.path.join('assets', file_name)).convert_alpha()

