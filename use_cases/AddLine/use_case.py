from typing import Tuple

from use_cases.presenter_abc import PresenterABC
from ..use_case_abc import UseCaseABC


class AddLine(UseCaseABC):
    def __init__(self, presenter: PresenterABC):
        UseCaseABC.__init__(self)
        self._presenter = presenter

    def configure(self, xy1: Tuple[int, int], xy2: Tuple[int, int], color='black', width=2, arrow_at_start=False,
                  arrow_at_end=False, tags=(), **_):
        arrow = None
        if arrow_at_start and arrow_at_end:
            arrow = 'both'
        elif arrow_at_start:
            arrow = 'start'
        elif arrow_at_end:
            arrow = 'end'
        self._response_model = {
            'xy1': xy1,
            'xy2': xy2,
            'color': color,
            'width': width,
            'tags': tags,
            'arrow': arrow, }

    def set_entities(self, entities):
        self._entities = entities

    def update_entities(self):
        pass

    def present(self):
        if self._presenter is None:
            return
        self._presenter.present(**self._response_model)
