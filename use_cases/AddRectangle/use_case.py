from typing import Tuple

from ..use_case_abc import UseCaseABC


class AddRectangle(UseCaseABC):
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
        shape_id = self._entities.rectangles.add(**self._configuration)
        self.create_response_model(shape_id)

    def create_response_model(self, shape_id, *args, **kwargs):
        self._response_model = self._entities.rectangles.get_configuration(shape_id)
