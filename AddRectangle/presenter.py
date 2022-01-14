from .use_case import PresenterABC


def presenter_factory():
    class PresenterAddRectangle(PresenterABC):
        def create_view_model(self):
            return self.response_model

    presenter = PresenterAddRectangle()
    return presenter
