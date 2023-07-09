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
            Piece.__init__(self, 1, "Pawn", piece_team, piece_square, "src/game_pieces/white_pawn.png")
        else:
            Piece.__init__(self, 1, "Pawn", piece_team, piece_square, "src/game_pieces/black_pawn.png")
    def __str__(self):
        return "Pawn:" + str(self.square) + ", Team:" + str(self.team)
class Rook(Piece):
    def __init__(self, piece_team: bool, piece_square):
        if piece_team:
            Piece.__init__(self, 5, "Rook", piece_team, piece_square, "src/game_pieces/white_rook.png")
        else:
            Piece.__init__(self, 5, "Rook", piece_team, piece_square, "src/game_pieces/black_rook.png")
    def __str__(self):
        return "Rook:" + str(self.square) + ", Team:" + str(self.team)
class Knight(Piece):
    def __init__(self, piece_team: bool, piece_square):
        if piece_team:
            Piece.__init__(self, 3, "Knight", piece_team, piece_square, "src/game_pieces/white_knight.png")
        else:
            Piece.__init__(self, 3, "Knight", piece_team, piece_square, "src/game_pieces/black_knight.png")
    def __str__(self):
        return "Knight:" + str(self.square) + ", Team:" + str(self.team)
class Bishop(Piece):
    def __init__(self, piece_team: bool, piece_square):
        if piece_team:
            Piece.__init__(self, 3, "Bishop", piece_team, piece_square, "src/game_pieces/white_bishop.png")
        else:
            Piece.__init__(self, 3, "Bishop", piece_team, piece_square, "src/game_pieces/black_bishop.png")
    def __str__(self):
        return "Bishop:" + str(self.square) + ", Team:" + str(self.team)
class King(Piece):
    def __init__(self, piece_team: bool, piece_square):
        if piece_team:
            Piece.__init__(self, 0, "King", piece_team, piece_square, "src/game_pieces/white_king.png")
        else:
            Piece.__init__(self, 0, "King", piece_team, piece_square, "src/game_pieces/black_king.png")
    def __str__(self):
        return "King:" + str(self.square) + ", Team:" + str(self.team)
class Queen(Piece):
    def __init__(self, piece_team: bool, piece_square):
        if piece_team:
            Piece.__init__(self, 9, "Queen", piece_team, piece_square, "src/game_pieces/white_queen.png")
        else:
            Piece.__init__(self, 9, "Queen", piece_team, piece_square, "src/game_pieces/black_queen.png")
    def __str__(self):
        return "Queen:" + str(self.square) + ", Team:" + str(self.team)



class GameManager():
    def __init__(self):
        # (0, 0) is top left
        self.board = np.empty((8, 8), dtype=Piece)

        side = False
        for i in [0, 7]:
            
            self.board[i][0] = Rook(side, (i, 0))
            self.board[i][1] = Knight(side, (i, 1))
            self.board[i][2] = Bishop(side, (i, 2))
            self.board[i][3] = Queen(side, (i, 3))
            self.board[i][4] = King(side, (i, 4))
            self.board[i][5] = Bishop(side, (i, 5))
            self.board[i][6] = Knight(side, (i, 6))
            self.board[i][7] = Rook(side, (i, 7))

            side = True

        for i in range(8):
            self.board[1][i] = Pawn(False, (0, i))
            self.board[6][i] = Pawn(True, (6, i))

    def __str__(self):
        return "The game manager"
    def get_board(self):
        return self.board
