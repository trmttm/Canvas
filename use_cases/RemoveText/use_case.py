from ..use_case_abc import UseCaseABC


class RemoveText(UseCaseABC):
    def configure(self, shape_id, **_):
        self._configuration = {'shape_id': shape_id}

    def update_entities(self):
        shape_id_passed = self._configuration.get('shape_id')
        shape_id = self._entities.texts.get_shape_ids_by_tag(shape_id_passed)[0]
        self._entities.texts.remove(shape_id)
        self.create_response_model()

    def create_response_model(self, *args, **kwargs):
        self._response_model = self._configuration
