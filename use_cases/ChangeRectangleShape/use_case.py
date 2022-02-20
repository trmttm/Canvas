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

    def present(self):
        self._presenter.present(**self._configuration)
