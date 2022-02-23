from use_cases.MoveRectangle.use_case import MoveRectangle
from use_cases.MoveText.use_case import MoveText
from use_cases.presenter_abc import PresenterABC
from use_cases_high_level.use_case_high_level import HighLevelUseCase


class MoveTextBox(HighLevelUseCase):
    def __init__(self, presenter: PresenterABC, entities):
        HighLevelUseCase.__init__(self, presenter, entities)
        self._sub_use_cases = [MoveRectangle(presenter, entities), MoveText(presenter, entities)]
