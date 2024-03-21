class Player:

    def __init__(self, team, taken_pieces = [], score = 0):
        # String which is either "White" or "Black"
        if (team != "White" or team != "Black"):
            raise ValueError(str(team) + " is not a valid team")
        self.team = team
        # Array of Piece
        self.taken_pieces = taken_pieces
        # number
        self.score = score