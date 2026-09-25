from typing import List

class ChessPiece:
    def __init__(self, name: str, positio: str, color: str):
        self.name = name
        self.position = positio
        self.color = color

    def display(self):
        return f"{self.color} {self.name} is at {self.position}"

class ChessBoard:
    def __init__(self):
        self.pieces: List[ChessPiece] = []

    def add_piece(self, piece: "ChessPiece"):
        self.pieces.append(piece)

    def display_board(self):
        print("current state of the chess board:")
        for piece in self.pieces:
            print(f".  {piece.display()}")

chess_board = ChessBoard()
piece1 = ChessPiece("King", "E1", "White")
piece2 = ChessPiece("Queen", "D1", "White")
piece3 = ChessPiece("Queen", "C1", "Black")
piece4 = ChessPiece("King", "F1", "Black")

chess_board = ChessBoard()
chess_board.add_piece(piece1)
chess_board.add_piece(piece2)
chess_board.add_piece(piece3)
chess_board.add_piece(piece4)

chess_board.display_board()

# Here comes the main part
# Now this board needs to be saved or have a checkpoint so that we can restore it later

new_chess_board = ChessBoard()
for p in chess_board.pieces:
    new_chess_board.add_piece(p)

print("_______________________")
new_chess_board.display_board()

# But this is manual copying of the chess board. If the chess board has a lot of pieces, 
# it will be very tedious to copy all the pieces manually.
# This code is messy and error prone

# The copying of piece should be handled by the ChessPiece class itself. 
# The ChessPiece class should have a method to clone itself and return a new instance of the same piece with the same properties.
#  This way, we can create a new chess board by cloning all the pieces from the original board.
