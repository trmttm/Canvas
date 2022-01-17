from view_tkinter import View
from view_tkinter import tk_interface as intf

from .ComplexCommands import package_names
from .main import App


def get_app(view_model=None) -> App:
    return App(lambda: app_tkinter_factory(view_model), package_names)


def app_tkinter_factory(view_model=None):
    view = View()
    if view_model is None:
        view_model = [
            intf.widget_model('root', 'canvas1', 'canvas', 0, 0, 0, 0, 'nsew', **{'bg': 'white'})
        ]
    view.add_widgets(view_model)
    view.switch_canvas('canvas1')
    return view
