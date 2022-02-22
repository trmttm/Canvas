from ..use_case import BaseUseCase


class SetBorderColor(BaseUseCase):
    def configure(self, shape_id, color, **_):
        self._configuration = {'shape_id': shape_id, 'color': color}

    def update_entities(self):
        shape_id = self._configuration.get('shape_id')
        color = self._configuration.get('color')
        self._entities.rectangles.set_border_color(shape_id, color)
