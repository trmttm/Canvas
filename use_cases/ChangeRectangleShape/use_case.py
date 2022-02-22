from ..use_case_abc import UseCaseABC


class ChangeRectangleShape(UseCaseABC):
    def configure(self, shape_id, coordinates_from, coordinates_to, **_):
        self._configuration = {'shape_id': shape_id, 'coordinates_from': coordinates_from,
                               'coordinates_to': coordinates_to}

    def update_entities(self):
        shape_id = self._configuration.get('shape_id')
        coordinates_from = self._configuration.get('coordinates_from')
        coordinates_to = self._configuration.get('coordinates_to')
        self._entities.rectangles.set_shape(shape_id, coordinates_from, coordinates_to)
        self.create_response_model()

    def create_response_model(self, *args, **kwargs):
        shape_id = self._configuration.get('shape_id')
        coordinates_from = self._entities.rectangles.get_coordinates_from(shape_id)
        coordinates_to = self._entities.rectangles.get_coordinates_to(shape_id)
        self._response_model = {'shape_id': shape_id, 'coordinates_from': coordinates_from,
                                'coordinates_to': coordinates_to}
