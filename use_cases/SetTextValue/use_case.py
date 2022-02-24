from ..use_case_abc import UseCaseABC


class SetTextValue(UseCaseABC):
    def configure(self, shape_id, text, **_):
        self._configuration = {'shape_id': shape_id, 'text': text}

    def update_entities(self):
        shape_id_passed = self._configuration.get('shape_id')
        shape_id = self._entities.texts.get_a_single_shape_id_by_tag(shape_id_passed)
        text = self._configuration.get('text')
        self._entities.texts.set_text(shape_id, text)
        self.create_response_model()

    def create_response_model(self, *args, **kwargs):
        shape_id_passed = self._configuration.get('shape_id')
        shape_id = self._entities.texts.get_a_single_shape_id_by_tag(shape_id_passed)
        text = self._entities.texts.get_text(shape_id)
        self._response_model = {'shape_id': shape_id, 'text': text}
