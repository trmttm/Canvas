from ..use_case_abc import UseCaseABC


class SetTextFontSize(UseCaseABC):
    def configure(self, shape_id, font_size, **_):
        self._configuration = {'shape_id': shape_id, 'font_size': font_size}

    def update_entities(self):
        shape_id = self._configuration.get('shape_id')
        font_size = self._configuration.get('font_size')
        self._entities.texts.set_font_size(shape_id, font_size)

    def present(self):
        if self._presenter is None:
            return
        self._presenter.present(**self._configuration)
