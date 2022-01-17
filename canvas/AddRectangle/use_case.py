from typing import Tuple

from .presenter_abc import PresenterABC


class AddRectangle:
    def __init__(self, presenter: PresenterABC = None, xy: Tuple[int, int] = (20, 20),
                 wh: Tuple[int, int] = (50, 20), border_color='black', border_width=2, fill='white', tags=(), **_):
        self._presenter = presenter
        self._xy = xy
        self._wh = wh
        self._border_color = border_color
        self._border_width = border_width
        self._fill = fill
        self._tags = tags

    def execute(self):
        if self._presenter is None:
            return
        self._presenter.present(self._xy, self._wh, self._border_color, self._border_width, self._fill, self._tags)