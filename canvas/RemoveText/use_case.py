from .presenter_abc import PresenterABC


class RemoveText:
    def __init__(self, presenter: PresenterABC, shape_id, **_):
        self._presenter = presenter
        self._shape_id = shape_id

    def execute(self):
        if self._presenter is None:
            return
        self._presenter.present(self._shape_id)
