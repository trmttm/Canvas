from entities.shapes.lines import Lines
from entities.shapes.rectangle import Rectangles
from entities.shapes.texts import Texts


class Entities:
    def __init__(self):
        self._rectangles = Rectangles()
        self._lines = Lines()
        self._texts = Texts()

    @property
    def rectangles(self) -> Rectangles:
        return self._rectangles

    @property
    def lines(self) -> Lines:
        return self._lines

    @property
    def texts(self) -> Texts:
        return self._texts
