from ..use_case_abc import UseCaseABC


class SetTextFontSize(UseCaseABC):
    def configure(self, shape_id, font_size, **_):
        self._configuration = {'shape_id': shape_id, 'font_size': font_size}

    def update_entities(self):
        pass

    def present(self):
        if self._presenter is None:
            return
        self._presenter.present(**self._configuration)
