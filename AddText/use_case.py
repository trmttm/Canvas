from typing import Tuple

from .presenter_abc import PresenterABC


class AddText:
    def __init__(self, presenter: PresenterABC = None, xy: Tuple[int, int] = (20, 20), text: str = 'text',
                 wh: Tuple[int, int] = (0, 0), text_rotation=0, tags=(),
                 **_):
        self._presenter = presenter
        self._xy = xy
        self._text = text
        self._wh = wh
        self._text_rotation = text_rotation
        self._tags = tags

    def execute(self):
        if self._presenter is None:
            return
        width, height = self._wh
        self._presenter.present(self._xy, self._text, width, height, self._text_rotation, self._tags)
