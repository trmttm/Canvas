from typing import Tuple

from entities.shapes.base_shape import Shapes


class Lines(Shapes):
    def add(self, xy1: tuple, xy2: tuple, color: str, width: int, arrow, tags: tuple, **options):
        options.update({
            'xy1': xy1,
            'xy2': xy2,
            'color': color,
            'width': width,
            'arrow': arrow,
            'tags': tags,
        })
        Shapes.add(self, **options)

    def get_xy1(self, shape_id):
        return self.get(shape_id, 'xy1')

    def get_xy2(self, shape_id):
        return self.get(shape_id, 'xy2')

    def get_color(self, shape_id):
        return self.get(shape_id, 'color')

    def get_width(self, shape_id):
        return self.get(shape_id, 'width')

    def get_arrow(self, shape_id):
        return self.get(shape_id, 'arrow')

    def get_tags(self, shape_id):
        return self.get(shape_id, 'tags')

    def get_x1(self, shape_id):
        return self._get_xy1(0, shape_id)

    def get_y1(self, shape_id):
        return self._get_xy1(1, shape_id)

    def get_x2(self, shape_id):
        return self._get_xy2(0, shape_id)

    def get_y2(self, shape_id):
        return self._get_xy2(1, shape_id)

    def set_xy1(self, shape_id, value: Tuple[int, int]):
        self.configure(shape_id, xy1=value)

    def set_x1(self, shape_id, value: int):
        y1 = self.get_y1(shape_id)
        self.configure(shape_id, xy1=(value, y1))

    def set_y1(self, shape_id, value: int):
        x1 = self.get_x1(shape_id)
        self.configure(shape_id, xy=(x1, value))

    def set_x2(self, shape_id, value: int):
        y2 = self.get_y2(shape_id)
        self.configure(shape_id, xy2=(value, y2))

    def set_y2(self, shape_id, value: int):
        x2 = self.get_x2(shape_id)
        self.configure(shape_id, xy=(x2, value))

    def set_color(self, shape_id, color):
        self.configure(shape_id, color=color)

    def set_width(self, shape_id, value):
        self.configure(shape_id, width=value)

    def set_arrow(self, shape_id, value):
        self.configure(shape_id, arrow=value)

    def _get_xy1(self, index_, shape_id):
        return self._get_pair_values(index_, 'xy1', shape_id)

    def _get_xy2(self, index_, shape_id):
        return self._get_pair_values(index_, 'xy2', shape_id)
