from ..use_case_abc import UseCaseABC


class SetLineColor(UseCaseABC):
    def configure(self, shape_id, color, **_):
        self._configuration = {'shape_id': shape_id, 'color': color}

    def update_entities(self):
        shape_id = self._configuration.get('shape_id')
        color = self._configuration.get('color')
        self._entities.lines.set_color(shape_id, color)
        self.create_response_model()

    def create_response_model(self, *args, **kwargs):
        shape_id = self._configuration.get('shape_id')
        color = self._entities.lines.get_color(shape_id)
        self._response_model = {'shape_id': shape_id, 'color': color}
