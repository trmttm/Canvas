from use_cases.presenter_abc import PresenterABC


class Presenter(PresenterABC):
    def present(self, shape_id, delta_x, delta_y, **_):
        self.response_model = {
            'shape_id': shape_id,
            'delta_x': delta_x,
            'delta_y': delta_y,
        }
        view_model = self.create_view_model()
        for observer in self._observers:
            observer(view_model)

    def create_view_model(self):
        rm = self.response_model
        view_model = {rm['shape_id']: (rm['delta_x'], rm['delta_y'])}
        return view_model


def presenter_factory():
    presenter = Presenter()
    return presenter
