from view_tkinter import View
from view_tkinter import tk_interface as intf


def app_tkinter_factory():
    view = View()
    view_model = [
        intf.widget_model('root', 'canvas1', 'canvas', 0, 0, 0, 0, 'nsew', **{'bg': 'light yellow'})
    ]
    view.add_widgets(view_model)
    view.switch_canvas('canvas1')
    return view
