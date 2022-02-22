from typing import Tuple

from ..use_case import BaseUseCase


class AddText(BaseUseCase):
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
        self._entities.texts.add(**self._configuration)
