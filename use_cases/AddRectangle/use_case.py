from typing import Tuple

from .presenter_abc import PresenterABC
from ..use_case_abc import UseCaseABC


class AddRectangle(UseCaseABC):
    def __init__(self, presenter: PresenterABC = None, xy: Tuple[int, int] = (20, 20),
                 wh: Tuple[int, int] = (50, 20), border_color='black', border_width=2, fill='white', tags=(), **_):
        UseCaseABC.__init__(self)

        self._presenter = presenter
        self._xy = xy
        self._wh = wh
        self._border_color = border_color
        self._border_width = border_width
        self._fill = fill
        self._tags = tags

    def set_entities(self, entities):
        self._entities = entities

    def update_entities(self):
        if self._presenter is None:
            return

        args = self._xy, self._wh, self._border_color, self._border_width, self._fill, self._tags
        self._update_entities(*args)
        self._presenter.present(*args)

    def _update_entities(self, *args, **kwargs):
        pass
