from abc import ABC, abstractmethod

class Piece(ABC):
    @abstractmethod
    def number_of_sides(self):
        pass