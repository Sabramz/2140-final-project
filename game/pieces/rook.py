import copy
from piece import Piece
import pygame
import os

class Rook(Piece):

    def __init__(self, team):
        super().__init__(team, "rook")
        self.moved = False

    # Each piece has a different set of possible moves.
    def possible_moves(self, board, pos, check_legal = True):
        moves = set()
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

        if check_legal:
            illegal_moves = set()
            for move in moves:
                new_board = copy.deepcopy(board)
                new_board.move_to(pos, move)
                if not new_board.is_legal(self.team):
                    illegal_moves.add(move)
            moves = moves.symmetric_difference(illegal_moves)
            
        return moves

    def move(self):
        self.moved = True

    def to_image(self):
        file_name = ""
        if self.team == "White":
            file_name = "w_rook.png"
        else:
            file_name = "b_rook.png"
        return pygame.image.load(os.path.join('assets', file_name)).convert_alpha()
    