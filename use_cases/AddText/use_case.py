from typing import Tuple

from ..use_case_abc import UseCaseABC


class AddText(UseCaseABC):
    def configure(self, xy: Tuple[int, int] = (20, 20), text: str = 'text', font_size: int = 13, color: str = 'black',
                  wh: Tuple[int, int] = (0, 0), text_rotation=0, tags=(), **_):
        self._configuration = {'xy': xy,
                               'text': text,
                               'font_size': font_size,
                               'color': color,
                               'wh': wh,
                               'text_rotation': text_rotation,
                               'tags': tags, }

    def update_entities(self):
        shape_id = self._entities.texts.add(**self._configuration)
        self.create_response_model(shape_id)

    def create_response_model(self, shape_id, *args, **kwargs):
        self._response_model = self._entities.texts.get_configuration(shape_id)
