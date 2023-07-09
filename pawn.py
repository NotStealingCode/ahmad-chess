from piece import Piece

class Pawn(Piece):
    def __init__(self):
        print("pawn created")

    def number_of_sides(self):
        print("4")