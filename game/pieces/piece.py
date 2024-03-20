from abc import ABC, abstractmethod

# An abstract piece in a game of Chess
class Piece(ABC):

    def __init__(self, x, y, team):
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
        # Boolean: True if piece on board, False if piece off board
        self.active = True
    
    # Each piece has a different set of possible moves.
    @abstractmethod
    def possible_moves(self, board):
        pass
        