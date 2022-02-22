from ..use_case import BaseUseCase


class MoveLine(BaseUseCase):
    def configure(self, shape_id, coordinates_from, coordinates_to, **_):
        self._configuration = {'shape_id': shape_id, 'coordinates_from': coordinates_from,
                               'coordinates_to': coordinates_to}

    def update_entities(self):
        shape_id = self._configuration.get('shape_id')
        coordinates_from = self._configuration.get('coordinates_from')
        coordinates_to = self._configuration.get('coordinates_to')
        self._entities.lines.set_xy1(shape_id, coordinates_from)
        self._entities.lines.set_xy1(shape_id, coordinates_to)
