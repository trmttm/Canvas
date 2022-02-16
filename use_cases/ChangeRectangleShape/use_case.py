from .presenter_abc import PresenterABC

from ..use_case_abc import UseCaseABC


class ChangeRectangleShape(UseCaseABC):
    def __init__(self, presenter: PresenterABC, shape_id, coordinates_from, coordinates_to, **_):
        UseCaseABC.__init__(self)
        
        self._presenter = presenter
        self._shape_id = shape_id
        self._coordinates_from = coordinates_from
        self._coordinates_to = coordinates_to

    def set_entities(self, entities):
        self._entities = entities

    def update_entities(self):
        if self._presenter is None:
            return

        args = self._shape_id, self._coordinates_from, self._coordinates_to
        self._update_entities(*args)
        self._presenter.present(*args)

    def _update_entities(self, *args, **kwargs):
        pass
