from use_cases.presenter_abc import PresenterABC


class Presenter(PresenterABC):
    def present(self, **response_model):
        shape_id = response_model.get('shape_id')
        x1, y1 = response_model.get('coordinates_from')
        x2, y2 = response_model.get('coordinates_to')
        view_model = {shape_id: (x1, y1, x2, y2)}
        for observer in self._observers:
            observer(view_model)


def presenter_factory():
    presenter = Presenter()
    return presenter
