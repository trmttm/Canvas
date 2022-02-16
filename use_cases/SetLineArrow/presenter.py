from use_cases.presenter_abc import PresenterABC


class Presenter(PresenterABC):
    def present(self, shape_id, arrow, **_):
        self.response_model = {shape_id: arrow, }
        view_model = self.create_view_model()
        for observer in self._observers:
            observer(view_model)

    def create_view_model(self):
        return self.response_model


def presenter_factory():
    presenter = Presenter()
    return presenter
