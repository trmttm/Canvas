from ..use_case_abc import UseCaseABC


class SetBorderColor(UseCaseABC):
    def configure(self, shape_id, color, **_):
        self._configuration = {'shape_id': shape_id, 'color': color}

    def update_entities(self):
        shape_id_passed = self._configuration.get('shape_id')
        shape_id = self._entities.rectangles.get_shape_ids_by_tag(shape_id_passed)[0]
        color = self._configuration.get('color')
        self._entities.rectangles.set_border_color(shape_id, color)
        self.create_response_model()

    def create_response_model(self, *args, **kwargs):
        shape_id_passed = self._configuration.get('shape_id')
        shape_id = self._entities.rectangles.get_shape_ids_by_tag(shape_id_passed)[0]
        color = self._entities.rectangles.get_border_color(shape_id)
        self._response_model = {'shape_id': shape_id, 'color': color}
