from .presenter_abc import PresenterABC


class RemoveRectangle:
    def __init__(self, presenter: PresenterABC, rectangle_id):
        self._presenter = presenter
        self._rectangle_id = rectangle_id

    def execute(self):
        if self._presenter is None:
            return
        self._presenter.present(self._rectangle_id)
