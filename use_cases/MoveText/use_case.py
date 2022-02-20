from ..use_case_abc import UseCaseABC


class MoveText(UseCaseABC):
    def configure(self, shape_id, delta_x, delta_y, **_):
        self._configuration = {'shape_id': shape_id, 'delta_x': delta_x, 'delta_y': delta_y}

    def update_entities(self):
        pass

    def present(self):
        self._presenter.present(**self._configuration)
