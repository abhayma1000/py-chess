import numpy as np

class Piece(): # piece_team TRUE = WHITE
    def __init__(self, piece_value, piece_name, piece_team, piece_square, piece_image_path):
        self.value = piece_value
        self.name = piece_name
        self.team = piece_team
        self.square = piece_square
        self.image_path = piece_image_path
    def can_move_to_square(self, new_square, board):
        # Can it move to a certain space --> Can legally move there, no teamate is there and an enemy is there, and not in check, doesnt put into check
        # Returns True/False
        return True # True for now
    def move_to_square(self, new_square, board):
        if self.can_move_to_square(new_square, board):
            self.square = new_square

            return True

            # If enemy is there, knock him out
        return None


class Pawn(Piece):
    def __init__(self, piece_team: bool, piece_square):
        if piece_team:
            Piece.__init__(self, 5, "Pawn", piece_team, piece_square, "")
        else:
            Piece.__init__(self, 5, "Pawn", piece_team, piece_square, "TODO other path")
    def __str__(self):
        return "Pawn:" + str(self.square) + ", Team:" + str(self.team)





class GameManager():
    def __init__(self):
        # (0, 0) is top left
        self.board = np.empty((8, 8), dtype=Piece)

        for i in range(8):
            self.board[0][i] = Pawn(False, (0, i))


        # TODO fill-in the board
    def __str__(self):
        return "The game manager"
    def get_board(self):
        return self.board
