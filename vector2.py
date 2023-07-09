class Vector2:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    # TODO: implement iterable
    # Make this type iterable to allow for object unpacking/destructoring
    def __iter__(self):
        return iter(self)