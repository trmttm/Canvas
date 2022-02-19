from ..use_case_abc import UseCaseABC


class RemoveLine(UseCaseABC):
    def configure(self, shape_id, **_):
        self._response_model = {'shape_id': shape_id}

    def update_entities(self):
        pass

    def present(self):
        self._presenter.present(**self._response_model)
