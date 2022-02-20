from ..use_case_abc import UseCaseABC


class SetLineArrow(UseCaseABC):
    def configure(self, shape_id, arrow, **_):
        self._configuration = {'shape_id': shape_id, 'arrow': arrow}

    def update_entities(self):
        pass

    def present(self):
        self._presenter.present(**self._configuration)
