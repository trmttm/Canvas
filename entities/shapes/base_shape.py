from typing import Any
from typing import Dict
from typing import Tuple


class ShapesCore:
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
        else:
            self._data[shape_id] = options

    def get(self, shape_id, option: str):
        individual_data = self._data.get(shape_id, None)
        if individual_data is not None:
            return individual_data.get(option, None)


class Shapes(ShapesCore):
    # ShapesCore with common implementations
    @property
    def shape_ids(self) -> tuple:
        return tuple(self._data.keys())

    def get_tags(self, shape_id):
        return self.get(shape_id, 'tags')

    def set_tags(self, shape_id, value):
        self.configure(shape_id, tags=value)

    def add_tag(self, shape_id, value):
        tags = self.get(shape_id, 'tags')
        tags += (value,)
        self.configure(shape_id, tags=tags)

    def remove_tag(self, shape_id, value):
        tags = self.get(shape_id, 'tags')
        new_tags = tuple(tag for tag in tags if tag != value)
        self.configure(shape_id, tags=new_tags)

    def get_shape_ids_by_tag(self, tag) -> tuple:
        shape_ids = set()
        for shape_id, data in self._data.items():
            tags = data['tags'] if 'tags' in data else ()
            if tag in tags:
                shape_ids.add(shape_id)
        return tuple(shape_ids)

    def _get_pair_values(self, index_: int, pair_key: str, shape_id):
        pair_values = self.get(shape_id, pair_key)
        return pair_values[index_] if pair_values is not None else None


class ShapesWithXY(Shapes):
    def get_xy(self, shape_id):
        return self.get(shape_id, 'xy')

    def get_x(self, shape_id):
        return self._get_xy(0, shape_id)

    def get_y(self, shape_id):
        return self._get_xy(1, shape_id)

    def _get_xy(self, index_, shape_id):
        return self._get_pair_values(index_, 'xy', shape_id)

    def _get_wh(self, index_, shape_id):
        return self._get_pair_values(index_, 'wh', shape_id)

    def set_xy(self, shape_id, value: Tuple[int, int]):
        self.configure(shape_id, xy=value)

    def set_x(self, shape_id, value: int):
        y = self.get_y(shape_id)
        self.configure(shape_id, xy=(value, y))

    def set_y(self, shape_id, value: int):
        x = self.get_x(shape_id)
        self.configure(shape_id, xy=(x, value))

    def move(self, shape_id, delta_x, delta_y):
        x, y = self.get_x(shape_id), self.get_y(shape_id)
        x += delta_x
        y += delta_y
        self.set_xy(shape_id, (x, y))


class ShapesWithXYWH(ShapesWithXY):
    def get_wh(self, shape_id):
        return self.get(shape_id, 'wh')

    def get_width(self, shape_id):
        return self._get_wh(0, shape_id)

    def get_height(self, shape_id):
        return self._get_wh(1, shape_id)

    def set_wh(self, shape_id, value: Tuple[int, int]):
        self.configure(shape_id, wh=value)

    def set_width(self, shape_id, value: int):
        height = self.get_height(shape_id)
        self.configure(shape_id, wh=(value, height))

    def set_height(self, shape_id, value: int):
        width = self.get_width(shape_id)
        self.configure(shape_id, wh=(width, value))
