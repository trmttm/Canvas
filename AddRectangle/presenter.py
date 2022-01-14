from .use_case import PresenterAddRectangleABC


def presenter_add_rectangle_factory():
    class PresenterAddRectangle(PresenterAddRectangleABC):
        def create_view_model(self):
            return self.response_model

    presenter = PresenterAddRectangle()
    return presenter
