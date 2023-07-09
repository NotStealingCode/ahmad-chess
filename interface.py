from engine import Engine
from engine import PieceType

class Interface:
    def __init__(self, engine: Engine):
        self.engine = engine

    def clear(self):
        print("\n")

    def convert_enum_to_alphabet(self, piece_type: PieceType):
        if piece_type == PieceType.PAWN:
            return "P"
        elif piece_type == PieceType.KNIGHT:
            return "N"
        elif piece_type == PieceType.BISHOP:
            return "B"
        elif piece_type == PieceType.ROOK:
            return "R"
        elif piece_type == PieceType.QUEEN:
            return "Q"
        elif piece_type == PieceType.KING:
            return "K"

    def draw(self):
        for i in range(8):
            for j in range(8):
                current_piece = self.engine.pieces[i][j]

                if not current_piece:
                    print("- ", end="")
                    continue

                print(self.convert_enum_to_alphabet(current_piece.type), "", end="")
            
            print()