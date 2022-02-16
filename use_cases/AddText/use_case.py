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
        width, height = self._wh

        args = self._xy, self._text, width, height, self._text_rotation, self._tags
        self._set_response_model(*args)

    def _set_response_model(self, *args, **kwargs):
        self._response_model = args

    def present(self):
        if self._presenter is None:
            return
        self._presenter.present(*self._response_model)
