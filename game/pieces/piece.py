from abc import ABC, abstractmethod

# An abstract piece in a game of Chess
class Piece(ABC):

    #                 row column   for debugging
    def __init__(self, x, y, team, name = ""):
        # number
        if x < 1 or x > 8:
            raise ValueError(str(x) + " is not a valid x value")
        self.x = x
        # number
        if y < 1 or y > 8:
            raise ValueError(str(y) + " is not a valid y value")
        self.y = y
        if team != "White" and team != "Black":
            raise ValueError(str(team) + " is not a valid team")
        self.team = team
        self.name = name
        # Boolean: True if piece on board, False if piece off board
        self.active = True

    def __repr__(self):
        return self.name
    
    # Each piece has a different set of possible moves.
    @abstractmethod
    def possible_moves(self, board):
        pass
    
    # definition of sameness for a piece
    def same_piece(self, piece):
        return self.x == piece.x and self.y == piece.y and self.team == piece.team

    def is_king(self):
        return False

    @abstractmethod
    def to_image(self):
        pass