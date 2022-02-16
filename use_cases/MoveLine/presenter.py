from use_cases.presenter_abc import PresenterABC


class Presenter(PresenterABC):
    def present(self, shape_id, coordinates_from, coordinates_to, **_):
        self.response_model = {
            'shape_id': shape_id,
            'coordinates_from': coordinates_from,
            'coordinates_to': coordinates_to,
        }
        view_model = self.create_view_model()
        for observer in self._observers:
            observer(view_model)

    def create_view_model(self):
        rm = self.response_model
        tag = rm['shape_id']
        x1, y1 = rm['coordinates_from']
        x2, y2 = rm['coordinates_to']
        view_model = {tag: (x1, y1, x2, y2)}
        return view_model


def presenter_factory():
    presenter = Presenter()
    return presenter
