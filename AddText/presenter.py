from .presenter_abc import PresenterABC


class Presenter(PresenterABC):
    def create_view_model(self):
        return self.response_model


def presenter_factory():
    presenter = Presenter()
    return presenter
