from typing import Any
from typing import Dict


class Selection:
    def select(self, shape_id):
        pass


class Shapes:
    def __init__(self):
        self._next_shape_id = 0
        self._data: Dict[Any, dict] = {}

    def add_text_box(self, **kwargs) -> int:
        self._next_shape_id += 1
        self._data[self._next_shape_id] = kwargs
        return self._next_shape_id

    @property
    def shape_ids(self) -> tuple:
        return tuple(self._data.keys())

    def configure(self, shape_id, **options):
        if shape_id in self._data:
            self._data[shape_id].update(options)


class Entities:
    def __init__(self):
        self._shapes = Shapes()
        self._selection = Selection()

    @property
    def shapes(self) -> Shapes:
        return self._shapes

    @property
    def selection(self) -> Selection:
        return self._selection
