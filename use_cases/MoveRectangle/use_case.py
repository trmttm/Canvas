from ..use_case_abc import UseCaseABC


class MoveRectangle(UseCaseABC):
    def configure(self, shape_id, delta_x, delta_y, **_):
        self._response_model = {'shape_id': shape_id, 'delta_x': delta_x, 'delta_y': delta_y}

    def update_entities(self):
        pass

    def present(self):
        if self._presenter is None:
            return
        self._presenter.present(**self._response_model)
