class Player:

    def __init__(self, team, pieces = [], taken_pieces = [], score = 0):
        # String which is either "White" or "Black"
        if team != "White" and team != "Black":
            raise ValueError(str(team) + " is not a valid team")
        self.team = team
        # Array of Piece
        self.pieces = pieces
        self.taken_pieces = taken_pieces
        # number
        self.score = score
    
    def take_piece(self, piece):
        for i in range(len(self.pieces)):
            if piece.same_piece(self.pieces[i]):
                self.taken_pieces.append(self.pieces.pop(i))
                return
        # if the program makes it here, then the piece was not present in the array
        raise ValueError(str(piece) + " is not one of the player's pieces")
    
