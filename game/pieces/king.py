import copy
from piece import Piece
import pygame
import os

class King(Piece):

    def __init__(self, team):
        super().__init__(team, "king")
        self.moved = False
    
    # Each piece has a different set of possible moves.
    def possible_moves(self, board, pos, check_legal = True):
        x = pos[0]
        y = pos[1]
        moves = set()
    
        if y + 1 <= 8:
            if board.moveable((x,y+1), self.team):
                moves.add((x, y + 1))
        if y - 1 >= 1:
            if board.moveable((x,y-1), self.team):
                moves.add((x, y - 1))
        if x + 1 <= 8:
            if board.moveable((x+1,y), self.team):
                moves.add((x + 1, y))
        if 1 <= x - 1:
            if board.moveable((x-1,y), self.team):
                moves.add((x - 1, y))

        if y + 1 <= 8 and x + 1 <= 8:
            if board.moveable((x+1,y+1), self.team):
                moves.add((x + 1, y + 1))
        if y - 1 >= 1 and x + 1 <= 8:
            if board.moveable((x+1,y-1), self.team):
                moves.add((x + 1, y - 1))
        if x - 1 <= 8 and y - 1 >= 1:
            if board.moveable((x-1,y-1), self.team):
                moves.add((x - 1, y - 1))
        if 1 <= x - 1 and y + 1 <= 8:
            if board.moveable((x-1,y+1), self.team):
                moves.add((x - 1, y + 1))

        # if king hasn't moved, it can castle
        if not self.moved:
            if self.team == "White":
                # queenside
                if not board.pieces[(1,1)].empty() and not board.pieces[(1,1)].moved and board.pieces[(2,1)].empty() and board.pieces[(3,1)].empty() and board.pieces[(4,1)].empty():
                    moves.add((x - 2, y))
                # kingside
                if not board.pieces[(8,1)].empty() and not board.pieces[(8,1)].moved and board.pieces[(6,1)].empty() and board.pieces[(7,1)].empty():
                    moves.add((x + 2, y))
            elif self.team == "Black":
                # queenside
                if not board.pieces[(1,8)].empty() and not board.pieces[(1,8)].moved and board.pieces[(2,8)].empty() and board.pieces[(3,8)].empty() and board.pieces[(4,8)].empty():
                    moves.add((x - 2, y))
                # king side
                if not board.pieces[(8,8)].empty() and not board.pieces[(8,8)].moved and board.pieces[(6,8)].empty() and board.pieces[(7,8)].empty():
                    moves.add((x + 2, y))

        if check_legal:
            illegal_moves = set()
            for move in moves:
                new_board = copy.deepcopy(board)
                new_board.move_to(pos, move)
                if not new_board.is_legal(self.team):
                    illegal_moves.add(move)
            moves = moves.symmetric_difference(illegal_moves)
        
        return moves
    
    # simply return king's possible moves without check for legality
    def king_moves(self, board, pos):
        x = pos[0]
        y = pos[1]
        moves = set()
    
        if y + 1 <= 8:
            if board.moveable((x,y+1), self.team):
                moves.add((x, y + 1))
        if y - 1 >= 1:
            if board.moveable((x,y-1), self.team):
                moves.add((x, y - 1))
        if x + 1 <= 8:
            if board.moveable((x+1,y), self.team):
                moves.add((x + 1, y))
        if 1 <= x - 1:
            if board.moveable((x-1,y), self.team):
                moves.add((x - 1, y))

        if y + 1 <= 8 and x + 1 <= 8:
            if board.moveable((x+1,y+1), self.team):
                moves.add((x + 1, y + 1))
        if y - 1 >= 1 and x + 1 <= 8:
            if board.moveable((x+1,y-1), self.team):
                moves.add((x + 1, y - 1))
        if x - 1 <= 8 and y - 1 >= 1:
            if board.moveable((x-1,y-1), self.team):
                moves.add((x - 1, y - 1))
        if 1 <= x - 1 and y + 1 <= 8:
            if board.moveable((x-1,y+1), self.team):
                moves.add((x - 1, y + 1))
            
        return moves
    
    # determine if this king is in check
    def in_check(self, board, pos):
        
        if self.team == "White":
            other_team_moves = board.possible_moves("Black", False)
        else:
            other_team_moves = board.possible_moves("White", False)

        return pos in other_team_moves

    # override
    def is_king(self):
        return True
    
    # override
    def move(self):
        self.moved = True

    def to_image(self):
        file_name = ""
        if self.team == "White":
            file_name = "w_king.png"
        else:
            file_name = "b_king.png"
        return pygame.image.load(os.path.join('assets', file_name)).convert_alpha()