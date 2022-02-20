from typing import Tuple

from entities.shapes.base_shape import Shapes


class Rectangles(Shapes):
    def add(self, xy: tuple = (20, 20), wh: tuple = (50, 20), fill: str = 'white', border_color: str = 'black',
            border_width: int = 1, tags=(), **options):
        options.update({
            'xy': xy,
            'wh': wh,
            'fill': fill,
            'border_color': border_color,
            'border_width': border_width,
            'tags': tags,
        })
        Shapes.add(self, **options)

    def get_xy(self, shape_id):
        return self.get(shape_id, 'xy')

    def get_wh(self, shape_id):
        return self.get(shape_id, 'wh')

    def get_fill_color(self, shape_id):
        return self.get(shape_id, 'fill')

    def get_border_width(self, shape_id):
        return self.get(shape_id, 'border_width')

    def get_tags(self, shape_id):
        return self.get(shape_id, 'tags')

    def get_x(self, shape_id):
        return self._get_xy(0, shape_id)

    def get_y(self, shape_id):
        return self._get_xy(1, shape_id)

    def get_width(self, shape_id):
        return self._get_wh(0, shape_id)

    def get_height(self, shape_id):
        return self._get_wh(1, shape_id)

    def set_xy(self, shape_id, value: Tuple[int, int]):
        self.configure(shape_id, xy=value)

    def set_x(self, shape_id, value: int):
        y = self.get_y(shape_id)
        self.configure(shape_id, xy=(value, y))

    def set_y(self, shape_id, value: int):
        x = self.get_x(shape_id)
        self.configure(shape_id, xy=(x, value))

    def set_wh(self, shape_id, value: Tuple[int, int]):
        self.configure(shape_id, wh=value)

    def set_width(self, shape_id, value: int):
        height = self.get_height(shape_id)
        self.configure(shape_id, wh=(value, height))

    def set_height(self, shape_id, value: int):
        width = self.get_width(shape_id)
        self.configure(shape_id, wh=(width, value))

    def set_fill_color(self, shape_id, color):
        self.configure(shape_id, fill=color)

    def set_border_color(self, shape_id, color):
        self.configure(shape_id, border_color=color)

    def set_border_width(self, shape_id, value):
        self.configure(shape_id, border_width=value)

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

    def _get_xy(self, index_, shape_id):
        return self._get_pair_values(index_, 'xy', shape_id)

    def _get_wh(self, index_, shape_id):
        return self._get_pair_values(index_, 'wh', shape_id)
