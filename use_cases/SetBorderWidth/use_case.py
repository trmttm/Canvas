from .presenter_abc import PresenterABC

from ..use_case_abc import UseCaseABC


class SetBorderWidth(UseCaseABC):
    def __init__(self, presenter: PresenterABC, shape_id, width, **_):
        self._presenter = presenter
        self._shape_id = shape_id
        self._width = width

    def set_entities(self, entities):
        self._entities = entities

    def update_entities(self):
        if self._presenter is None:
            return

        args = self._shape_id, self._width
        self._update_entities(*args)
        self._presenter.present(*args)

    def _update_entities(self, *args, **kwargs):
        pass
