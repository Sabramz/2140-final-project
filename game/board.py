from game.pieces.pawn import Pawn
from game.pieces.king import King
from game.pieces.queen import Queen
from game.pieces.bishop import Bishop
from game.pieces.knight import Knight
from game.pieces.rook import Rook

SQUARE_SIZE = 60

class Board:

    # Initialize the board to a new game of chess
    def __init__(self):
        self.pieces = { \
            (1,8): Rook(1,8, "Black"), (2,8): Knight(2, 8, "Black"), (3, 8): Bishop(3,8, "Black"), (4, 8): Queen(4, 8, "Black"), \
            (5,8): King(5,8, "Black"), (6,8): Bishop(6, 8, "Black"), (7, 8): Knight(7,8, "Black"), (8, 8): Rook(8, 8, "Black"), \
            (1,7): Pawn(1,7,"Black"), (2,7): Pawn(2, 7, "Black"), (3,7): Pawn(3, 7, "Black"), (4,7): Pawn(4, 7, "Black"), \
            (5,7): Pawn(5, 7, "Black"), (6,7): Pawn(6, 7, "Black"), (7,7): Pawn(7, 7, "Black"), (8,7): Pawn(8, 7, "Black"), \
            (1,2): Pawn(1,2,"White"), (2,2): Pawn(2, 2, "White"), (3,2): Pawn(3, 2, "White"), (4,2): Pawn(4, 2, "White"), \
            (5,2): Pawn(5, 2, "White"), (6,2): Pawn(6, 2, "White"), (7,2): Pawn(7, 2, "White"), (8,2): Pawn(8, 2, "White"), \
            (1,1): Rook(1,1, "White"), (2,1): Knight(2, 1, "White"), (3, 1): Bishop(3,1, "White"), (4, 1): Queen(4, 1, "White"), \
            (5,1): King(5,1, "White"), (6,1): Bishop(6, 1, "White"), (7, 1): Knight(7,1, "White"), (8, 1): Rook(8, 1, "White") \
        }

    # get piece at position
    def get_piece(self, pos):
        if not pos in self.pieces:
            raise ValueError("There is no piece at " + str(pos))
        return pos

    # determine if a square is open
    # pos is a tuple (x, y)
    def open_square(self, pos):
        return pos in self.pieces
    
    # determine if a piece at a square is on your team
    # pos is a tuple (x, y)
    def teamate_present(self, piece, pos):
        if not self.open_square(pos):
            other_piece = self.get_piece(pos)
            return piece.team == other_piece.team
        return False

    # Check to see if there is a checkmate on the board. True
    # def checkmate(self):
    #     # imp: check to see if each king is in the possible moves of another piece
    #     # if so, check to see if it has any possible moves. If not, 
    #     kings = []
    #     for piece in self.pieces:
    #         if piece.is_king():
    #             kings.append(piece)
    #     for k in kings:
    #         if len(k.possible_moves()) == 0:
    #             return k.team

        

    # Get all of the possible moves of one team
    def team_possible_moves(self, team):
        possible_moves = set()
        for piece in self.pieces:
            if piece.team == team:
                possible_moves.update(set(piece.possible_moves()))
        return possible_moves
        
    # return the board as an image for pygame to display
    def piece_images(self, white_turn):
        images = []
        if not white_turn:
            for pos, piece in self.pieces.items():
                images.append((piece.to_image(), (pos[0] * SQUARE_SIZE, pos[1] * SQUARE_SIZE)))
        else:
            for pos, piece in self.pieces.items():
                images.append((piece.to_image(), (pos[0] * SQUARE_SIZE, (9 - pos[1]) * SQUARE_SIZE)))
        return images

