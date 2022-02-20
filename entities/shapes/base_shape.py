from typing import Any
from typing import Dict


class Shapes:
    def __init__(self):
        self._next_id = 0
        self._data: Dict[Any, dict] = {}

    def add(self, **options) -> int:
        self._next_id += 1
        self._data[self._next_id] = options
        return self._next_id

    def remove(self, shape_id):
        if shape_id in self._data:
            del self._data[shape_id]

    def set(self, data: dict[Any, dict]):
        self._data = data

    def configure(self, shape_id, **options):
        if shape_id in self._data:
            self._data[shape_id].update(options)

    def get(self, shape_id, option: str):
        individual_data = self._data.get(shape_id, None)
        if individual_data is not None:
            return individual_data.get(option, None)

    @property
    def shape_ids(self) -> tuple:
        return tuple(self._data.keys())
