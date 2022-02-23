from typing import List

from use_cases.SetBorderColor.use_case import SetBorderColor
from use_cases.SetBorderWidth.use_case import SetBorderWidth
from use_cases.SetFillColor.use_case import SetFillColor
from use_cases.SetTextColor.use_case import SetTextColor
from use_cases.presenter_abc import PresenterABC
from use_cases.use_case_abc import UseCaseABC
from use_cases_high_level.use_case_high_level import HighLevelUseCase


class HighlightTextBox(HighLevelUseCase):
    def __init__(self, presenter: PresenterABC, entities):
        HighLevelUseCase.__init__(self, presenter, entities)
        self._sub_use_cases: List[UseCaseABC, ...] = [SetFillColor(presenter, entities),
                                                      SetBorderColor(presenter, entities),
                                                      SetBorderWidth(presenter, entities),
                                                      SetTextColor(presenter, entities),
                                                      ]
