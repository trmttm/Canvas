from use_cases.presenter_abc import PresenterABC


class Presenter(PresenterABC):
    def present(self, **response_model):
        view_model = {
            'width': response_model.get('wh', (0, 0))[0],
            'height': response_model.get('wh', (0, 0))[1],
            'x': response_model.get('xy', (0, 0))[0],
            'y': response_model.get('xy', (0, 0))[1],
            'border_color': response_model.get('border_color'),
            'border_width': response_model.get('border_width'),
            'fill': response_model.get('fill'),
            'tags': response_model.get('tags'),
        }
        for observer in self._observers:
            observer(view_model)


def presenter_factory():
    presenter = Presenter()
    return presenter
