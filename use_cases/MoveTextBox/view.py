from interface_view import ViewABC

from use_cases.MoveRectangle.view import view_factory as view_factory_01
from use_cases.MoveText.view import view_factory as view_factory_02


def view_factory(app: ViewABC):
    def view_method(view_model: dict):
        view_factory_01(app)(view_model[1])
        view_factory_02(app)(view_model[2])

    return view_method
