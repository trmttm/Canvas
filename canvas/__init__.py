from view_tkinter import View
from view_tkinter import tk_interface as intf

from .AddRectangle.request_model import get_request_model as rm0
from .RemoveRectangle.request_model import get_request_model as rm1
from .MoveRectangle.request_model import get_request_model as rm2
from .SetBorderColor.request_model import get_request_model as rm3
from .SetBorderWidth.request_model import get_request_model as rm4
from .SetFillColor.request_model import get_request_model as rm5
from .AddText.request_model import get_request_model as rm6
from .SetTextColor.request_model import get_request_model as rm7
from .SetTextFontSize.request_model import get_request_model as rm8
from .MoveText.request_model import get_request_model as rm9
from .RemoveText.request_model import get_request_model as rm10
from .AddLine.request_model import get_request_model as rm11
from .MoveLine.request_model import get_request_model as rm12
from .RemoveLine.request_model import get_request_model as rm13
from .SetLineWidth.request_model import get_request_model as rm14
from .SetLineColor.request_model import get_request_model as rm15
from .SetLineArrow.request_model import get_request_model as rm16
from .ChangeRectangleShape.request_model import get_request_model as rm17
from .app import App

package_names = [
    'canvas.AddRectangle',  # 0
    'canvas.RemoveRectangle',  # 1
    'canvas.MoveRectangle',  # 2
    'canvas.SetBorderColor',  # 3
    'canvas.SetBorderWidth',  # 4
    'canvas.SetFillColor',  # 5
    'canvas.AddText',  # 6
    'canvas.SetTextColor',  # 7
    'canvas.SetTextFontSize',  # 8
    'canvas.MoveText',  # 9
    'canvas.RemoveText',  # 10
    'canvas.AddLine',  # 11
    'canvas.MoveLine',  # 12
    'canvas.RemoveLine',  # 13
    'canvas.SetLineWidth',  # 14
    'canvas.SetLineColor',  # 15
    'canvas.SetLineArrow',  # 16
    'canvas.ChangeRectangleShape'  # 17
]


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
