from interface_view import ViewABC

from use_cases.SetBorderColor.view import view_factory as view_factory_02
from use_cases.SetBorderWidth.view import view_factory as view_factory_03
from use_cases.SetFillColor.view import view_factory as view_factory_01
from use_cases.SetTextColor.view import view_factory as view_factory_04


def view_factory(app: ViewABC):
    def view_method(view_model: dict):
        view_factory_01(app)(view_model[1])
        view_factory_02(app)(view_model[2])
        view_factory_03(app)(view_model[3])
        view_factory_04(app)(view_model[4])

    return view_method
