from typing import List

from use_cases.AddRectangle.use_case import AddRectangle
from use_cases.AddText.use_case import AddText
from use_cases.presenter_abc import PresenterABC
from use_cases.use_case_abc import UseCaseABC
from use_cases_high_level.use_case_high_level import HighLevelUseCase


class AddTextBox(HighLevelUseCase):
    def __init__(self, presenter: PresenterABC, entities):
        HighLevelUseCase.__init__(self, presenter, entities)
        self._sub_use_cases: List[UseCaseABC, ...] = [AddRectangle(presenter, entities), AddText(presenter, entities)]
