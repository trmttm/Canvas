from .presenter_abc import PresenterABC

from ..use_case_abc import UseCaseABC


class RemoveRectangle(UseCaseABC):
    def __init__(self, presenter: PresenterABC, shape_id, **_):
        self._presenter = presenter
        self._shape_id = shape_id

    def set_entities(self, entities):
        self._entities = entities

    def update_entities(self):
        if self._presenter is None:
            return

        args = (self._shape_id,)
        self._update_entities(*args)
        self._presenter.present(*args)

    def _update_entities(self, *args, **kwargs):
        pass
