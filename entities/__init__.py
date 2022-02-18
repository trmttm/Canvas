class Selection:
    def select(self, shape_id):
        pass


class Shapes:
    def __init__(self):
        self._next_shape_id = 0
        self._data = {}

    def add_text_box(self, **kwargs) -> int:
        self._next_shape_id += 1
        self._data[self._next_shape_id] = kwargs
        return self._next_shape_id


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
