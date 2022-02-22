from ..use_case_abc import UseCaseABC


class SetBorderWidth(UseCaseABC):
    def configure(self, shape_id, width, **_):
        self._configuration = {'shape_id': shape_id, 'width': width}

    def update_entities(self):
        shape_id = self._configuration.get('shape_id')
        width = self._configuration.get('width')
        self._entities.rectangles.set_border_width(shape_id, width)
        self.create_response_model()

    def create_response_model(self, *args, **kwargs):
        shape_id = self._configuration.get('shape_id')
        width = self._entities.rectangles.get_border_width(shape_id)
        self._response_model = {'shape_id': shape_id, 'width': width}
