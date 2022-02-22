from ..use_case import BaseUseCase


class RemoveLine(BaseUseCase):
    def configure(self, shape_id, **_):
        self._configuration = {'shape_id': shape_id}

    def update_entities(self):
        shape_id = self._configuration.get('shape_id')
        self._entities.lines.remove(shape_id)
