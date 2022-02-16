from .presenter_abc import PresenterABC
from ..use_case_abc import UseCaseABC


class MoveRectangle(UseCaseABC):
    def __init__(self, presenter: PresenterABC, shape_id, delta_x, delta_y, **_):
        self._presenter = presenter
        self._shape_id = shape_id
        self._delta_x = delta_x
        self._delta_y = delta_y

    def set_entities(self, entities):
        self._entities = entities

    def execute(self):
        if self._presenter is None:
            return
        self._presenter.present(self._shape_id, self._delta_x, self._delta_y)
