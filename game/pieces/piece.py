from abc import ABC, abstractmethod

# An abstract piece in a game of Chess
class Piece(ABC):

    #                  String String
    def __init__(self, team,  name = ""):
        if team != "White" and team != "Black" and team != "empty":
            raise ValueError(str(team) + " is not a valid team")
        self.team = team
        self.name = name
        self.moved = False

    # this piece's string representation (for debugging)
    def __repr__(self):
        return self.name
    
    # Each piece has a different set of possible moves.
    @abstractmethod
    def possible_moves(self, board, pos, check_legal = True):
        pass
    
    # definition of sameness for a piece
    def same_piece(self, piece):
        return self.team == piece.team and self.name == self.name

    # determine if this piece is a king
    def is_king(self):
        return False

    # determine if this piece is a pawn
    def is_pawn(self):
        return False

    # return this piece as a pygame surface
    @abstractmethod
    def to_image(self):
        pass

    # to determine if this piece is an empty piece
    def empty(self):
        return False

    # to update the movement state of this piece
    def move(self):
        pass
    