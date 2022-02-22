from use_cases.RemoveRectangle.use_case import RemoveRectangle
from use_cases.RemoveText.use_case import RemoveText
from ..presenter_abc import PresenterABC
from ..use_case_high_level import HighLevelUseCase


class MoveTextBox(HighLevelUseCase):
    def __init__(self, presenter: PresenterABC, entities):
        HighLevelUseCase.__init__(self, presenter, entities)
        self._sub_use_cases = [RemoveRectangle(presenter, entities), RemoveText(presenter, entities)]
