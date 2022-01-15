from .presenter_abc import PresenterABC


class Presenter(PresenterABC):
    def create_view_model(self):
        rm = self.response_model
        view_model = {rm['rectangle_id']: (rm['delta_x'], rm['delta_y'])}
        return view_model


def presenter_factory():
    presenter = Presenter()
    return presenter
