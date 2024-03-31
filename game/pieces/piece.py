from abc import ABC, abstractmethod

# An abstract piece in a game of Chess
class Piece(ABC):

    #                 row column   for debugging
    def __init__(self, team, name):
        if team != "White" and team != "Black" and team != "empty":
            raise ValueError(str(team) + " is not a valid team")
        self.team = team
        self.name = name
        self.moved = False

    def __repr__(self):
        return self.name
    
    # Each piece has a different set of possible moves.
    @abstractmethod
    def possible_moves(self, board, pos, check_legal = True):
        pass

    # Returns the set of squares that this pieces protects (incl teamates)
    # @abstractmethod
    def protects(self, board, pos):
        return self.possible_moves(board, pos)
    
    # definition of sameness for a piece
    def same_piece(self, piece):
        return self.team == piece.team and self.name == self.name

    def is_king(self):
        return False

    def is_pawn(self):
        return False

    @abstractmethod
    def to_image(self):
        pass

    def empty(self):
        return False

    def move(self):
        pass
    