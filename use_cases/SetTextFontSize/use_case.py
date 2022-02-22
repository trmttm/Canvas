from ..use_case_abc import UseCaseABC


class SetTextFontSize(UseCaseABC):
    def configure(self, shape_id, font_size, **_):
        self._configuration = {'shape_id': shape_id, 'font_size': font_size}

    def update_entities(self):
        shape_id = self._configuration.get('shape_id')
        font_size = self._configuration.get('font_size')
        self._entities.texts.set_font_size(shape_id, font_size)
        self.create_response_model()

    def create_response_model(self, *args, **kwargs):
        shape_id = self._configuration.get('shape_id')
        font_size = self._entities.texts.get_font_size(shape_id)
        self._response_model = {'shape_id': shape_id, 'font_size': font_size}
