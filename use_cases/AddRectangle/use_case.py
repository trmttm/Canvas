from typing import Tuple

from use_cases.presenter_abc import PresenterABC
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
        args = self._xy, self._wh, self._border_color, self._border_width, self._fill, self._tags
        self._set_response_model(*args)

    def _set_response_model(self, *args, **kwargs):
        self._response_model = args

    def present(self):
        if self._presenter is None:
            return
        self._presenter.present(*self._response_model)
