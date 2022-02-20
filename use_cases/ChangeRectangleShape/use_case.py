from ..use_case_abc import UseCaseABC


class ChangeRectangleShape(UseCaseABC):
    def configure(self, shape_id, coordinates_from, coordinates_to, **_):
        self._configuration = {'shape_id': shape_id, 'coordinates_from': coordinates_from,
                               'coordinates_to': coordinates_to}

    def update_entities(self):
        shape_id = self._configuration.get('shape_id')
        x1, y1 = self._configuration.get('coordinates_from')
        x2, y2 = self._configuration.get('coordinates_to')
        wh = x2 - x1, y2 - y1
        self._entities.rectangles.set_xy(shape_id, (x1, y1))
        self._entities.rectangles.set_wh(shape_id, wh)

    def present(self):
        self._presenter.present(**self._configuration)
