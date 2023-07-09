from enum import Enum
from vector2 import Vector2

class PieceColor(Enum):
    WHITE = 1,
    BLACK = 2

class PieceType(Enum):
    PAWN = 1,
    KNIGHT = 2,
    BISHOP = 3,
    ROOK = 4,
    QUEEN = 5,
    KING = 6

class Piece:
    def __init__(self, piece_color: PieceColor, piece_type: PieceType):
        self.color = piece_color
        self.type = piece_type

class Engine:
    def __init__(self):
        self.running = True
        self.selected_piece = None # TODO: unused
        self.pieces = [
            [Piece(PieceColor.WHITE, PieceType.ROOK),Piece(PieceColor.WHITE, PieceType.KNIGHT),Piece(PieceColor.WHITE, PieceType.BISHOP),Piece(PieceColor.WHITE, PieceType.QUEEN),Piece(PieceColor.WHITE, PieceType.KING),Piece(PieceColor.WHITE, PieceType.BISHOP),Piece(PieceColor.WHITE, PieceType.KNIGHT),Piece(PieceColor.WHITE, PieceType.ROOK)],
            [Piece(PieceColor.WHITE, PieceType.PAWN),Piece(PieceColor.WHITE, PieceType.PAWN),Piece(PieceColor.WHITE, PieceType.PAWN),Piece(PieceColor.WHITE, PieceType.PAWN),Piece(PieceColor.WHITE, PieceType.PAWN),Piece(PieceColor.WHITE, PieceType.PAWN),Piece(PieceColor.WHITE, PieceType.PAWN),Piece(PieceColor.WHITE, PieceType.PAWN)],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [Piece(PieceColor.BLACK, PieceType.PAWN),Piece(PieceColor.BLACK, PieceType.PAWN),Piece(PieceColor.BLACK, PieceType.PAWN),Piece(PieceColor.BLACK, PieceType.PAWN),Piece(PieceColor.BLACK, PieceType.PAWN),Piece(PieceColor.BLACK, PieceType.PAWN),Piece(PieceColor.BLACK, PieceType.PAWN),Piece(PieceColor.BLACK, PieceType.PAWN)],
            [Piece(PieceColor.BLACK, PieceType.ROOK),Piece(PieceColor.BLACK, PieceType.KNIGHT),Piece(PieceColor.BLACK, PieceType.BISHOP),Piece(PieceColor.BLACK, PieceType.QUEEN),Piece(PieceColor.BLACK, PieceType.KING),Piece(PieceColor.BLACK, PieceType.BISHOP),Piece(PieceColor.BLACK, PieceType.KNIGHT),Piece(PieceColor.BLACK, PieceType.ROOK)]
        ]

    def update(self):
        print("game engine update")

    # TODO: Make unit tests for this function
    # a1 = [0,0]
    # a2 = [0,1]
    # b1 = [1,0]
    def convert_SAN_to_position(self, SAN: str):
        letter = SAN[0]
        number = int(SAN[1])
        
        new_x = ord(letter) % 97 # TODO: get rid of magic number 97 which represents the letter 'a' ordinal value
        new_y = number - 1

        return Vector2(new_x, new_y)
    
    # TODO: implement this if needed
    # def convert_position_to_SAN(self, position: Vector2):


    # TODO: consider moving this into its own class
    def get_available_moves(self, SAN: str):
        # TODO: use object destructoring here
        position = self.convert_SAN_to_position(SAN)
        current_piece = self.pieces[position.x][position.y]

        # return empty array if location chosen is not a piece
        if not current_piece:
            return []

        print("Display the moves for:", current_piece.type, current_piece.color)
        available_moves = []
        if current_piece.type == PieceType.PAWN:
            