from piece import Piece
import pygame

class Empty(Piece):

    def __init__(self):
        super().__init__("empty", "empty")
    
    # Each piece has a different set of possible moves.
    def possible_moves(self, board, pos, check_legal):
        return set([])
    
    def protects(self, board, pos):
        return set([])

    def to_image(self):
        return None

    def empty(self):
        return True
    

    
    