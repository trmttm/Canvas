from .presenter_abc import PresenterABC


class MoveRectangle:
    def __init__(self, presenter: PresenterABC, rectangle_id, delta_x, delta_y, **_):
        self._presenter = presenter
        self._rectangle_id = rectangle_id
        self._delta_x = delta_x
        self._delta_y = delta_y

    def execute(self):
        if self._presenter is None:
            return
        self._presenter.present(self._rectangle_id, self._delta_x, self._delta_y)
