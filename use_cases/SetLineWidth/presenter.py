from use_cases.SetLineWidth.view_model import create_view_model
from use_cases.presenter_abc import PresenterABC


class Presenter(PresenterABC):
    def present(self, **response_model):
        view_model = self.create_view_model(response_model)
        for observer in self._observers:
            observer(view_model)

    def create_view_model(self, response_model):
        return create_view_model(response_model)


def presenter_factory():
    presenter = Presenter()
    return presenter
