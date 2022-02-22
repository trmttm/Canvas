from ..use_case import BaseUseCase


class SetLineWidth(BaseUseCase):
    def configure(self, shape_id, width, **_):
        self._configuration = {'shape_id': shape_id, 'width': width}

    def update_entities(self):
        shape_id = self._configuration.get('shape_id')
        width = self._configuration.get('width')
        self._entities.lines.set_width(shape_id, width)
