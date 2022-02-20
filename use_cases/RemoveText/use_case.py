from ..use_case_abc import UseCaseABC


class RemoveText(UseCaseABC):
    def configure(self, shape_id, **_):
        self._configuration = {'shape_id': shape_id}

    def update_entities(self):
        shape_id = self._configuration.get('shape_id')
        self._entities.texts.remove(shape_id)

    def present(self):
        self._presenter.present(**self._configuration)
