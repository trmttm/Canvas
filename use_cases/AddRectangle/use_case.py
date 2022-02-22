from typing import Tuple

from ..use_case import BaseUseCase


class AddRectangle(BaseUseCase):
    def configure(self, xy: Tuple[int, int] = (20, 20), wh: Tuple[int, int] = (50, 20), border_color='black',
                  border_width=2, fill='white', tags=(), **_):
        self._configuration = {
            'xy': xy,
            'wh': wh,
            'border_color': border_color,
            'border_width': border_width,
            'fill': fill,
            'tags': tags,
        }

    def update_entities(self):
        self._entities.rectangles.add(**self._configuration)
