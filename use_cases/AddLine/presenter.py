from use_cases.presenter_abc import PresenterABC


class Presenter(PresenterABC):
    def present(self, **response_model):
        view_model = {
            response_model.get('tags'): {'coordinate_from': response_model.get('xy1'),
                                         'coordinate_to': response_model.get('xy2'),
                                         'line_color': response_model.get('color'),
                                         'line_width': response_model.get('width'),
                                         'tags': response_model.get('tags')}
        }
        for observer in self._observers:
            observer(view_model)


def presenter_factory():
    presenter = Presenter()
    return presenter
