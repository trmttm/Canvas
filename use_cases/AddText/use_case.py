from typing import Tuple

from .presenter_abc import PresenterABC
from ..use_case_abc import UseCaseABC


class AddText(UseCaseABC):
    def __init__(self, presenter: PresenterABC = None, xy: Tuple[int, int] = (20, 20), text: str = 'text',
                 wh: Tuple[int, int] = (0, 0), text_rotation=0, tags=(),
                 **_):
        UseCaseABC.__init__(self)

        self._presenter = presenter
        self._xy = xy
        self._text = text
        self._wh = wh
        self._text_rotation = text_rotation
        self._tags = tags

    def set_entities(self, entities):
        self._entities = entities

    def update_entities(self):
        if self._presenter is None:
            return
        width, height = self._wh

        args = self._xy, self._text, width, height, self._text_rotation, self._tags
        self._update_entities(*args)
        self._presenter.present(*args)

    def _update_entities(self, *args, **kwargs):
        pass
