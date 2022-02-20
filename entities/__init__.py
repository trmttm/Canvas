from entities.shapes.rectangle import Rectangles


class Entities:
    def __init__(self):
        self._rectangles = Rectangles()

    @property
    def rectangles(self) -> Rectangles:
        return self._rectangles
