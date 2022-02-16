from typing import Tuple

from .presenter_abc import PresenterABC
from ..use_case_abc import UseCaseABC


class AddLine(UseCaseABC):
    def __init__(self, presenter: PresenterABC, xy1: Tuple[int, int], xy2: Tuple[int, int], color='black', width=2,
                 arrow_at_start=False, arrow_at_end=False, tags=(), **_):
        UseCaseABC.__init__(self)

        self._presenter = presenter
        self._xy1 = xy1
        self._xy2 = xy2
        self._color = color
        self._width = width
        self._tags = tags
        self._arrow = None
        if arrow_at_start and arrow_at_end:
            self._arrow = 'both'
        elif arrow_at_start:
            self._arrow = 'start'
        elif arrow_at_end:
            self._arrow = 'end'

    def set_entities(self, entities):
        self._entities = entities

    def update_entities(self):
        if self._presenter is None:
            return

        args = self._xy1, self._xy2, self._color, self._width, self._tags, self._arrow
        self._update_entities(*args)

    def _update_entities(self, *args, **kwargs):
        self._response_model = args

    def present(self):
        self._presenter.present(*self._response_model)
