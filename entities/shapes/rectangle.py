from typing import Tuple

from entities.shapes.base_shape import ShapesWithTagsXYWH


class Rectangles(ShapesWithTagsXYWH):
    def __init__(self):
        ShapesWithTagsXYWH.__init__(self, tag_prefix='rectangle_')

    def add(self, xy: tuple = (20, 20), wh: tuple = (50, 20), fill: str = 'white', border_color: str = 'black',
            border_width: int = 1, tags=(), **options) -> str:
        options.update({
            'xy': xy,
            'wh': wh,
            'fill': fill,
            'border_color': border_color,
            'border_width': border_width,
            'tags': tags,
        })
        shape_id = ShapesWithTagsXYWH.add(self, **options)
        return shape_id

    def get_fill_color(self, shape_id):
        return self.get(shape_id, 'fill')

    def set_fill_color(self, shape_id, color):
        self.configure(shape_id, fill=color)

    def get_border_width(self, shape_id):
        return self.get(shape_id, 'border_width')

    def set_border_width(self, shape_id, value):
        self.configure(shape_id, border_width=value)

    def get_border_color(self, shape_id):
        return self.get(shape_id, 'border_color')

    def set_border_color(self, shape_id, color):
        self.configure(shape_id, border_color=color)

    def set_shape(self, shape_id, coordinates_from: Tuple[int, int], coordinates_to: Tuple[int, int]):
        x1, y1 = coordinates_from
        x2, y2 = coordinates_to
        wh = x2 - x1, y2 - y1
        self.set_xy(shape_id, (x1, y1))
        self.set_wh(shape_id, wh)
