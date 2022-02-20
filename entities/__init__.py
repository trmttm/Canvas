from entities.shapes.lines import Lines
from entities.shapes.rectangle import Rectangles


class Entities:
    def __init__(self):
        self._rectangles = Rectangles()
        self._lines = Lines()

    @property
    def rectangles(self) -> Rectangles:
        return self._rectangles

    @property
    def lines(self) -> Lines:
        return self._lines
