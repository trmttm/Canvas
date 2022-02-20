from ..use_case_abc import UseCaseABC


class SetFillColor(UseCaseABC):
    def configure(self, shape_id, color, **_):
        self._configuration = {'shape_id': shape_id, 'color': color}

    def update_entities(self):
        shape_id = self._configuration.get('shape_id')
        color = self._configuration.get('color')
        self._entities.rectangles.set_fill_color(shape_id, color)

    def present(self):
        self._presenter.present(**self._configuration)
