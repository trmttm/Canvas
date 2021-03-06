from typing import Tuple

from entities.shapes.base_shape import ShapesWithTagsXYWH


class Texts(ShapesWithTagsXYWH):
    def __init__(self):
        ShapesWithTagsXYWH.__init__(self, tag_prefix='text_')

    def add(self, xy: Tuple[int, int] = (20, 20), text: str = 'text', color: str = 'black',
            wh: Tuple[int, int] = (0, 0), text_rotation=0, font_size=13, tags=(), **options) -> str:
        options.update({
            'xy': xy,
            'wh': wh,
            'text': text,
            'color': color,
            'text_rotation': text_rotation,
            'font_size': font_size,
            'tags': tags,
        })
        shape_id = ShapesWithTagsXYWH.add(self, **options)
        return shape_id

    def get_text(self, shape_id):
        return self.get(shape_id, 'text')

    def set_text(self, shape_id, text: str):
        self.configure(shape_id, text=text)

    def get_color(self, shape_id):
        return self.get(shape_id, 'color')

    def set_color(self, shape_id, color: str):
        self.configure(shape_id, color=color)

    def get_text_rotation(self, shape_id):
        return self.get(shape_id, 'text_rotation')

    def set_text_rotation(self, shape_id, text_rotation: int):
        self.configure(shape_id, text_rotation=text_rotation)

    def get_font_size(self, shape_id):
        return self.get(shape_id, 'font_size')

    def set_font_size(self, shape_id, font_size: int):
        self.configure(shape_id, font_size=font_size)
