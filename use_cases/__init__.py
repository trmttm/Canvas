from .AddLine.request_model import get_request_model as get_request_model_for_add_line
from .AddRectangle.request_model import get_request_model as get_request_model_for_add_rectangle
from .AddText.request_model import get_request_model as get_request_model_for_add_text
from .AddTextBox.request_model import get_request_model as get_request_model_for_add_text_box
from .ChangeRectangleShape.request_model import get_request_model as get_request_model_for_change_rectangle_shape
from .MoveLine.request_model import get_request_model as get_request_model_for_move_line
from .MoveRectangle.request_model import get_request_model as get_request_model_for_move_rectangle
from .MoveText.request_model import get_request_model as get_request_model_for_move_text
from .MoveTextBox.request_model import get_request_model as get_request_model_for_move_text_box
from .RemoveLine.request_model import get_request_model as get_request_model_for_remove_line
from .RemoveRectangle.request_model import get_request_model as get_request_model_for_remove_rectangle
from .RemoveText.request_model import get_request_model as get_request_model_for_remove_text
from .RemoveTextBox.request_model import get_request_model as get_request_model_for_remove_text_box
from .SetBorderColor.request_model import get_request_model as get_request_model_for_set_border_color
from .SetBorderWidth.request_model import get_request_model as get_request_model_for_set_border_width
from .SetFillColor.request_model import get_request_model as get_request_model_for_set_fill_color
from .SetLineArrow.request_model import get_request_model as get_request_model_for_set_line_arrow
from .SetLineColor.request_model import get_request_model as get_request_model_for_set_line_color
from .SetLineWidth.request_model import get_request_model as get_request_model_for_set_line_with
from .SetTextColor.request_model import get_request_model as get_request_model_for_set_text_color
from .SetTextFontSize.request_model import get_request_model as get_request_model_for_set_text_font_size

AddLine = 'use_cases.AddLine'
AddRectangle = 'use_cases.AddRectangle'
AddText = 'use_cases.AddText'
AddTextBox = 'use_cases.AddTextBox'
ChangeRectangleShape = 'use_cases.ChangeRectangleShape'
MoveLine = 'use_cases.MoveLine'
MoveRectangle = 'use_cases.MoveRectangle'
MoveText = 'use_cases.MoveText'
MoveTextBox = 'use_cases.MoveTextBox'
RemoveLine = 'use_cases.RemoveLine'
RemoveRectangle = 'use_cases.RemoveRectangle'
RemoveText = 'use_cases.RemoveText'
RemoveTextBox = 'use_cases.RemoveTextBox'
SetBorderColor = 'use_cases.SetBorderColor'
SetBorderWidth = 'use_cases.SetBorderWidth'
SetFillColor = 'use_cases.SetFillColor'
SetLineArrow = 'use_cases.SetLineArrow'
SetLineColor = 'use_cases.SetLineColor'
SetLineWidth = 'use_cases.SetLineWidth'
SetTextColor = 'use_cases.SetTextColor'
SetTextFontSize = 'use_cases.SetTextFontSize'

package_names = [
    AddRectangle,  # 0
    RemoveRectangle,  # 1
    MoveRectangle,  # 2
    SetBorderColor,  # 3
    SetBorderWidth,  # 4
    SetFillColor,  # 5
    AddText,  # 6
    SetTextColor,  # 7
    SetTextFontSize,  # 8
    MoveText,  # 9
    RemoveText,  # 10
    AddLine,  # 11
    MoveLine,  # 12
    RemoveLine,  # 13
    SetLineWidth,  # 14
    SetLineColor,  # 15
    SetLineArrow,  # 16
    ChangeRectangleShape,  # 17
    # Higher Level UseCases
    AddTextBox,  # 18
    RemoveTextBox,  # 19
    MoveTextBox,  # 20
]
