from typing import List

from ..SetBorderColor.use_case import SetBorderColor
from ..SetBorderWidth.use_case import SetBorderWidth
from ..SetFillColor.use_case import SetFillColor
from ..SetTextColor.use_case import SetTextColor
from ..presenter_abc import PresenterABC
from ..use_case_abc import UseCaseABC
from ..use_case_high_level import HighLevelUseCase


class HighlightTextBox(HighLevelUseCase):
    def __init__(self, presenter: PresenterABC, entities):
        HighLevelUseCase.__init__(self, presenter, entities)
        self._sub_use_cases: List[UseCaseABC, ...] = [SetFillColor(presenter, entities),
                                                      SetBorderColor(presenter, entities),
                                                      SetBorderWidth(presenter, entities),
                                                      SetTextColor(presenter, entities),
                                                      ]
