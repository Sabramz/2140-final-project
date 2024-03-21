from game.pieces.pawn import Pawn

class Board:

    def __init__(self, pieces = []):
        self.pieces = pieces
    
    # Make a new game of chess
    def new_game(self):
        self.pieces = [ \
            Pawn(1, 7, "Black"), Pawn(2, 7, "Black"), Pawn(3, 7, "Black"), Pawn(4, 7, "Black"), Pawn(5, 7, "Black"), Pawn(6, 7, "Black"), Pawn(7, 7, "Black"), Pawn(8, 7, "Black"), \ 
            Pawn(1, 2, "White"), Pawn(2, 2, "White"), Pawn(3, 2, "White"), Pawn(4, 2, "White"), Pawn(5, 2, "White"), Pawn(6, 2, "White"), Pawn(7, 2, "White"), Pawn(8, 2, "White"), \
        ]


    # get piece at position
    def get_piece(self, x, y):
        for i in range(len(self.pieces)):
            piece = self.pieces[i]
            if piece[i].x == x and piece[i].y == y:
                return piece
        # No piece at the position
        return None

    # determine if a square is open
    def open_square(self, x, y):
        for i in range(len(self.pieces)):
            piece = self.pieces[i]
            if piece[i].x == x and piece[i].y == y:
                return False
        True

    # Check to see if there is a checkmate on the board
    def checkmate(self):
        pass
