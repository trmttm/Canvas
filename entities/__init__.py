from typing import List
from typing import Tuple

from entities.group import Group
from entities.shapes.base_shape import Shapes
from entities.shapes.lines import Lines
from entities.shapes.rectangle import Rectangles
from entities.shapes.texts import Texts


class Entities:
    def __init__(self):
        self._rectangles = Rectangles()
        self._lines = Lines()
        self._texts = Texts()
        self._group = Group()

        self._shape_entities: List[Shapes] = [self._rectangles, self._lines, self._texts]

    @property
    def shape_entities(self) -> Tuple[Shapes]:
        return tuple(self._shape_entities)

    @property
    def rectangles(self) -> Rectangles:
        return self._rectangles

    @property
    def lines(self) -> Lines:
        return self._lines

    @property
    def texts(self) -> Texts:
        return self._texts

    @property
    def group(self) -> Group:
        return self._group
