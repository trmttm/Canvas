from ..use_case_abc import UseCaseABC


class MoveRectangle(UseCaseABC):
    def configure(self, shape_id, delta_x, delta_y, **_):
        self._configuration = {'shape_id': shape_id, 'delta_x': delta_x, 'delta_y': delta_y}

    def update_entities(self):
        shape_id = self._configuration.get('shape_id')
        delta_x = self._configuration.get('delta_x')
        delta_y = self._configuration.get('delta_y')
        self._entities.rectangles.move(shape_id, delta_x, delta_y)

    def present(self):
        if self._presenter is None:
            return
        self._presenter.present(**self._configuration)
