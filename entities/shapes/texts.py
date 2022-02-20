from typing import Tuple

from entities.shapes.base_shape import ShapesWithXYWH


class Texts(ShapesWithXYWH):
    def add(self, xy: Tuple[int, int] = (20, 20), text: str = 'text', wh: Tuple[int, int] = (0, 0),
            text_rotation=0, tags=(), **options):
        options.update({
            'xy': xy,
            'wh': wh,
            'text': text,
            'text_rotation': text_rotation,
            'tags': tags,
        })
        ShapesWithXYWH.add(self, **options)

    def get_text(self, shape_id):
        return self.get(shape_id, 'text')

    def set_text(self, shape_id, text: str):
        self.configure(shape_id, text=text)

    def get_text_rotation(self, shape_id):
        return self.get(shape_id, 'text_rotation')

    def set_text_rotation(self, shape_id, text_rotation: int):
        self.configure(shape_id, text_rotation=text_rotation)
