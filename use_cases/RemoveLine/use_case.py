from ..use_case_abc import UseCaseABC


class RemoveLine(UseCaseABC):
    def configure(self, shape_id, **_):
        self._configuration = {'shape_id': shape_id}

    def update_entities(self):
        shape_id = self._configuration.get('shape_id')
        self._entities.lines.remove(shape_id)
        self.create_response_model()

    def create_response_model(self, *args, **kwargs):
        self._response_model = self._configuration
