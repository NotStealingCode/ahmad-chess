from piece import Piece

class Rook(Piece):
    def __init__(self):
        print("rook created")

    def number_of_sides(self):
        print("8")