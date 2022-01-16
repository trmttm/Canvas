from .presenter_abc import PresenterABC


class MoveLine:
    def __init__(self, presenter: PresenterABC, shape_id, coordinates_from, coordinates_to, **_):
        self._presenter = presenter
        self._shape_id = shape_id
        self._coordinates_from = coordinates_from
        self._coordinates_to = coordinates_to

    def execute(self):
        if self._presenter is None:
            return
        self._presenter.present(self._shape_id, self._coordinates_from, self._coordinates_to)
