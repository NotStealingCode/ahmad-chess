from engine import Engine
from interface import Interface
from vector2 import Vector2

def main():
    engine = Engine()
    interface = Interface(engine)

    engine.get_available_moves("a1")

    # Game Loop
    while engine.running:
        engine.update()
        interface.draw()
        break

if __name__ == "__main__":
    main()