from typing import Tuple

from .presenter_abc import PresenterABC


class AddText:
    def __init__(self, presenter: PresenterABC = None, xy: Tuple[int, int] = (20, 20), text: str = 'text', tags=(),
                 **_):
        self._presenter = presenter
        self._xy = xy
        self._text = text
        self._tags = tags

    def execute(self):
        if self._presenter is None:
            return
        self._presenter.present(self._xy, self._text, self._tags)
