from use_cases.AddRectangle.use_case import AddRectangle
from use_cases.AddText.use_case import AddText
from ..presenter_abc import PresenterABC
from ..use_case_high_level import HighLevelUseCase


class AddTextBox(HighLevelUseCase):
    def __init__(self, presenter: PresenterABC, entities):
        HighLevelUseCase.__init__(self, presenter, entities)
        self._sub_use_cases = [AddRectangle(presenter, entities), AddText(presenter, entities)]
