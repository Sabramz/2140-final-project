from piece import Piece
import pygame
import os

class Queen(Piece):

    def __init__(self, team):
        super().__init__(team, "queen")

    
    # Each piece has a different set of possible moves.
    def possible_moves(self, board, pos):
        moves = set()
        x = pos[0]
        y = pos[1]
        flag = False
        # up right
        while x < 8 and y < 8 and not flag:
            x += 1
            y += 1
            # If there is a piece in the way, it can be taken, but this Bishop cannot move past it
            if board.moveable((x, y), self.team):
                moves.add((x,y))
                if board.enemy_piece((x,y), self.team):
                    flag = True
            else:
                break
        x = pos[0]
        y = pos[1]
        flag = False
        # down right
        while x < 8 and 1 < y and not flag:
            x += 1
            y -= 1
            if board.moveable((x, y), self.team):
                moves.add((x,y))
                if board.enemy_piece((x,y), self.team):
                    flag = True
            else:
                break
        x = pos[0]
        y = pos[1]
        flag = False
        # down left
        while 1 < x and 1 < y  and not flag:
            x -= 1
            y -= 1
            if board.moveable((x, y), self.team):
                moves.add((x,y))
                if board.enemy_piece((x,y), self.team):
                    flag = True
            else:
                break
        x = pos[0]
        y = pos[1]
        flag = False
        # up left
        while 1 < x and y < 8 and not flag:
            x -= 1
            y += 1
            if board.moveable((x, y), self.team):
                moves.add((x,y))
                if board.enemy_piece((x,y), self.team):
                    flag = True
            else:
                break
            moves.add((x,y))


        x = pos[0]
        y = pos[1]
        flag = False
        # up
        while y < 8 and not flag:
            y += 1
            # If there is a piece in the way, it can be taken, but this Rook cannot move past it
            if board.moveable((x, y), self.team):
                moves.add((x,y))
                if board.enemy_piece((x,y), self.team):
                    flag = True
            else:
                break
        y = pos[1]
        flag = False
        # right
        while x < 8 and not flag:
            x += 1
            if board.moveable((x, y), self.team):
                moves.add((x,y))
                if board.enemy_piece((x,y), self.team):
                    flag = True
            else:
                break
        x = pos[0]
        flag = False
        #down
        while 1 < y and not flag:
            y -= 1
            if board.moveable((x, y), self.team):
                moves.add((x,y))
                if board.enemy_piece((x,y), self.team):
                    flag = True
            else:
                break
        y = pos[1]
        flag = False
        #left
        while 1 < x and not flag:
            x -= 1
            if board.moveable((x, y), self.team):
                moves.add((x,y))
                if board.enemy_piece((x,y), self.team):
                    flag = True
            else:
                break

        return moves

    def to_image(self):
        file_name = ""
        if self.team == "White":
            file_name = "w_queen.png"
        else:
            file_name = "b_queen.png"
        return pygame.image.load(os.path.join('assets', file_name)).convert_alpha()