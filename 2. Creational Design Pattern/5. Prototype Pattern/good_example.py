from typing import List
import copy

class ChessPiece:
    def __init__(self, name: str, positio: str, color: str):
        self.name = name
        self.position = positio
        self.color = color

    def display(self):
        return f"{self.color} {self.name} is at {self.position}"

    def clone(self) -> "ChessPiece":
        return copy.deepcopy(self)  # Create a deep copy of the current instancee
                                    # This ensures that all attributes of the object are copied,
                                    #  and any mutable objects within the instance are also copied,
                                    #  preventing shared references between the original and cloned objects.
class ChessBoard:
    def __init__(self):
        self.pieces: List[ChessPiece] = []

    def add_piece(self, piece: "ChessPiece"):
        self.pieces.append(piece)

    def display_board(self):
        print("current state of the chess board:")
        for piece in self.pieces:
            print(f".  {piece.display()}")

    def clone(self):
        return copy.deepcopy(self)
      # Create a deep copy of the current instance
# A normal copy of the chess board would only copy the references to the pieces,
#  so if we modify a piece in the original board, it would also affect the cloned board. 
# By using deepcopy, we ensure that the cloned board has its own copies of the pieces, 
# and any modifications to the original board will not affect the cloned board.


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

new_chess_board = chess_board.clone()  # Create a deep copy of the chess board using the clone method

print("_______________________")
new_chess_board.add_piece(ChessPiece("Bishop", "C1", "White"))  # Add a new piece to the cloned board
new_chess_board.display_board()