from .presenter_abc import PresenterABC


class Presenter(PresenterABC):
    def create_view_model(self):
        view_model = {
            self.response_model['tags']: self.response_model,
        }
        return view_model


def presenter_factory():
    presenter = Presenter()
    return presenter
