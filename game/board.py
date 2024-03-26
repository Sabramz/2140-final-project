from game.pieces.pawn import Pawn
from game.pieces.king import King
from game.pieces.queen import Queen
from game.pieces.bishop import Bishop
from game.pieces.knight import Knight
from game.pieces.rook import Rook
from game.pieces.empty import Empty

SQUARE_SIZE = 60

class Board:

    # Initialize the board to a new game of chess
    def __init__(self):
        self.pieces = { \
            (1,8): Rook("Black"), (2,8): Knight("Black"), (3, 8): Bishop("Black"), (4, 8): Queen("Black"), (5,8): King("Black"), (6,8): Bishop("Black"), (7, 8): Knight("Black"), (8, 8): Rook("Black"), \
            (1,7): Pawn("Black"), (2,7): Pawn("Black"), (3,7): Pawn("Black"), (4,7): Pawn("Black"), (5,7): Pawn("Black"), (6,7): Pawn("Black"), (7,7): Pawn("Black"), (8,7): Pawn("Black"), \
            





            (1,2): Pawn("White"), (2,2): Pawn("White"), (3,2): Pawn("White"), (4,2): Pawn("White"), (5,2): Pawn("White"), (6,2): Pawn("White"), (7,2): Pawn("White"), (8,2): Pawn("White"), \
            (1,1): Rook("White"), (2,1): Knight("White"), (3, 1): Bishop("White"), (4, 1): Queen("White"), (5,1): King("White"), (6,1): Bishop("White"), (7, 1): Knight("White"), (8, 1): Rook("White") \
        }
        for x in range(1, 9):
            for y in range(3, 7):
                self.pieces[(x, y)] = Empty()

    # get piece at position
    def get_piece(self, pos):
        if pos not in self.pieces:
            return
        return self.pieces[pos]
    
    # get possible moves of piece
    def get_possible_moves(self, pos):
        if pos not in self.pieces:
            return []
        return self.pieces[pos].possible_moves(self, pos)

    # determine if a square is open
    def open_square(self, x, y):
        return self.pieces[(x, y)].empty()
    
    # determine if an enemy piece is at a position
    def enemy_piece(self, pos, team):
        if team == "White":
            if pos in self.pieces:
                if self.pieces[pos].team == "Black":
                    return True
        elif team == "Black":
            if pos in self.pieces:
                if self.pieces[pos].team == "White":
                    return True
        return False
    
    # determine if a piece can move to a square
    def moveable(self, pos, team):
        return self.open_square(pos[0], pos[1]) or self.enemy_piece(pos, team)
    
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
        for pos, piece in self.pieces.items():
            if piece.team == team and not piece.is_king():
                possible_moves.update(piece.possible_moves(self, pos))
        return possible_moves
        
    # return the board as an image for pygame to display
    def piece_images(self, white_turn):
        images = []
        if not white_turn:
            for pos, piece in self.pieces.items():
                image = piece.to_image()
                if image != None:
                    images.append((image, [8 - pos[0], pos[1] - 1]))
        else:
            for pos, piece in self.pieces.items():
                image = piece.to_image()
                if image != None:
                    images.append((image, [pos[0] - 1, 8 - pos[1]]))
        return images

    def move_to(self, pos, square):
        self.pieces[pos].move()
        self.pieces[square] = self.pieces[pos]
        self.pieces[pos] = Empty()
        return True
