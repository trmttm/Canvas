from ..use_case_abc import UseCaseABC


class SetFillColor(UseCaseABC):
    def configure(self, shape_id, color, **_):
        self._response_model = {'shape_id': shape_id, 'color': color}

    def update_entities(self):
        pass

    def present(self):
        self._presenter.present(**self._response_model)
