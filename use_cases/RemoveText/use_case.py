from .presenter_abc import PresenterABC

from ..use_case_abc import UseCaseABC


class RemoveText(UseCaseABC):
    def __init__(self, presenter: PresenterABC, shape_id, **_):
        self._presenter = presenter
        self._shape_id = shape_id

    def set_entities(self, entities):
        self._entities = entities

    def execute(self):
        if self._presenter is None:
            return
        self._presenter.present(self._shape_id)
