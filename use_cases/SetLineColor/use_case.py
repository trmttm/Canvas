from ..use_case_abc import UseCaseABC


class SetLineColor(UseCaseABC):
    def configure(self, shape_id, color, **_):
        self._configuration = {'shape_id': shape_id, 'color': color}

    def update_entities(self):
        pass

    def present(self):
        self._presenter.present(**self._configuration)
