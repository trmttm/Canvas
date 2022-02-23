from typing import Tuple

from ..use_case_abc import UseCaseABC


class MoveRectangle(UseCaseABC):
    def configure(self, shape_id, delta_x, delta_y, **_):
        self._configuration = {'shape_id': shape_id, 'delta_x': delta_x, 'delta_y': delta_y}

    def update_entities(self):
        shape_id_passed = self._configuration.get('shape_id')
        shape_id = self._entities.rectangles.get_shape_ids_by_tag(shape_id_passed)[0]
        coordinates_from = self._entities.rectangles.get_coordinates_from(shape_id)
        delta_x = self._configuration.get('delta_x')
        delta_y = self._configuration.get('delta_y')
        self._entities.rectangles.move(shape_id, delta_x, delta_y)
        self.create_response_model(coordinates_from)

    def create_response_model(self, coordinates_from: Tuple[int, int], *args, **kwargs):
        shape_id_passed = self._configuration.get('shape_id')
        shape_id = self._entities.rectangles.get_shape_ids_by_tag(shape_id_passed)[0]
        x1, y1 = coordinates_from
        x2, y2 = self._entities.rectangles.get_xy(shape_id)
        delta_x, delta_y = x2 - x1, y2 - y1
        self._response_model = {'shape_id': shape_id, 'delta_x': delta_x, 'delta_y': delta_y}
