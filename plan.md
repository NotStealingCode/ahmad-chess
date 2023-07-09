How I want the game to play:

- Black -
    a b c d e f g h
--------------------
8 | R N B Q K B N R
7 | P P P P P P P
6 | - - - - - - - -
5 | - - - - - - - -
4 | - - - - - - - -
3 | - - - - - - - -
2 | P P P P P P P P
1 | R N B Q K B N R
- White -

-> White: Select a piece
  - a2

-> Available moves: a3, a4
  - a4

- Black -
    a b c d e f g h
--------------------
8 | R N B Q K B N R
7 | P P P P P P P
6 | - - - - - - - -
5 | - - - - - - - -
4 | P - - - - - - -
3 | - - - - - - - -
2 | - P P P P P P P
1 | R N B Q K B N R
- White -


-> Black: Select a piece
  - a7

-> Available moves: a5, a6
  - a5


- Black -
    a b c d e f g h
--------------------
8 | R N B Q K B N R
7 | - P P P P P P
6 | - - - - - - - -
5 | P - - - - - - -
4 | P - - - - - - -
3 | - - - - - - - -
2 | - P P P P P P P
1 | R N B Q K B N R
- White -

====

main
```python
def main():
  engine = Engine()
  interface = Interface(engine)
```
- Engine()
- Interface

Engine
- positions[Piece][Piece] // we store these here so each piece can easily have a look-up of the whole map
- def game_loop()
  - loop here while checking for user input

- def convert_user_to_coord() // converts a1 to 0,0
```python
def __init__(self):
  self.pieces = [Piece][Piece]
  
  self.pieces[0][0] = Piece(Color::White, Piece::Rook)

def game_loop(self):

def check_available_moves(self, Vector2):
  // this method could probably be moved to another class, depending on complexity

def convert_input_to_position(self):
```

Interface
- def clear()
- def draw(positions)
  - clear()

```python
def __init__(self, engine: Engine):
  self.engine = engine

def clear(self):
  print("\n"*100)

def draw(self):
  for i in range():
    for j in range():
      print(engine[i][j])
```

Piece
- const color: Color::Black || Color::White (Enum)
- const type: Piece::KING || PIECE::QUEEN || PIECE::ROOK || PIECE::BISHOP || PIECE::KNIGHT
- position: Vector2(x, y)

// why do we store the position of the pieces outside of the particular piece objects?
  // the pieces don't use their positions for anything
Pawn(Piece)
- __init__(color)

Vector2
- x: int
- y: int


========================

        # self.pieces = [
        #     [Piece(PieceColor.BLACK, PieceType.ROOK),Piece(PieceColor.BLACK, PieceType.KNIGHT),Piece(PieceColor.BLACK, PieceType.BISHOP),Piece(PieceColor.BLACK, PieceType.QUEEN),Piece(PieceColor.BLACK, PieceType.KING),Piece(PieceColor.BLACK, PieceType.BISHOP),Piece(PieceColor.BLACK, PieceType.KNIGHT),Piece(PieceColor.BLACK, PieceType.ROOK)],
        #     [Piece(PieceColor.BLACK, PieceType.PAWN),Piece(PieceColor.BLACK, PieceType.PAWN),Piece(PieceColor.BLACK, PieceType.PAWN),Piece(PieceColor.BLACK, PieceType.PAWN),Piece(PieceColor.BLACK, PieceType.PAWN),Piece(PieceColor.BLACK, PieceType.PAWN),Piece(PieceColor.BLACK, PieceType.PAWN),Piece(PieceColor.BLACK, PieceType.PAWN)],
        #     [None,None,None,None,None,None,None,None],
        #     [None,None,None,None,None,None,None,None],
        #     [None,None,None,None,None,None,None,None],
        #     [None,None,None,None,None,None,None,None],
        #     [Piece(PieceColor.WHITE, PieceType.PAWN),Piece(PieceColor.WHITE, PieceType.PAWN),Piece(PieceColor.WHITE, PieceType.PAWN),Piece(PieceColor.WHITE, PieceType.PAWN),Piece(PieceColor.WHITE, PieceType.PAWN),Piece(PieceColor.WHITE, PieceType.PAWN),Piece(PieceColor.WHITE, PieceType.PAWN),Piece(PieceColor.WHITE, PieceType.PAWN)],
        #     [Piece(PieceColor.WHITE, PieceType.ROOK),Piece(PieceColor.WHITE, PieceType.KNIGHT),Piece(PieceColor.WHITE, PieceType.BISHOP),Piece(PieceColor.WHITE, PieceType.QUEEN),Piece(PieceColor.WHITE, PieceType.KING),Piece(PieceColor.WHITE, PieceType.BISHOP),Piece(PieceColor.WHITE, PieceType.KNIGHT),Piece(PieceColor.WHITE, PieceType.ROOK)]
        # ]
    

=======
things i tried/notes
- my python version doens't support switch statements
- try to get rid of None later
- add explicit types for linter
- run this through a linter


keywords:
- destructoring/unpacking
- enum
- implicit types
- creating my own iterable object
- abstract classes
- type aliases (didnt use this yet)