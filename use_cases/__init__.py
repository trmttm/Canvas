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
    'use_cases.AddRectangle',  # 0
    'use_cases.RemoveRectangle',  # 1
    'use_cases.MoveRectangle',  # 2
    'use_cases.SetBorderColor',  # 3
    'use_cases.SetBorderWidth',  # 4
    'use_cases.SetFillColor',  # 5
    'use_cases.AddText',  # 6
    'use_cases.SetTextColor',  # 7
    'use_cases.SetTextFontSize',  # 8
    'use_cases.MoveText',  # 9
    'use_cases.RemoveText',  # 10
    'use_cases.AddLine',  # 11
    'use_cases.MoveLine',  # 12
    'use_cases.RemoveLine',  # 13
    'use_cases.SetLineWidth',  # 14
    'use_cases.SetLineColor',  # 15
    'use_cases.SetLineArrow',  # 16
    'use_cases.ChangeRectangleShape'  # 17
]


def get_app(view_model=None) -> App:
    return App(lambda: app_tkinter_factory(view_model), package_names)


def app_tkinter_factory(view_model=None):
    view = View()
    if view_model is None:
        view_model = [
            intf.widget_model('root', 'canvas1', 'use_cases', 0, 0, 0, 0, 'nsew', **{'bg': 'white'})
        ]
    view.add_widgets(view_model)
    view.switch_canvas('canvas1')
    return view
