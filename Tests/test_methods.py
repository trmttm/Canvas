from request_models import get_request_model_for_add_line
from request_models import get_request_model_for_add_rectangle
from request_models import get_request_model_for_add_text
from request_models import get_request_model_for_add_text_box
from use_cases.AddLine.presenter import presenter_factory as presenter_factory_02
from use_cases.AddLine.use_case import AddLine
from use_cases.AddLine.view import view_factory as view_factory_02
from use_cases.AddRectangle.presenter import presenter_factory as presenter_factory_03
from use_cases.AddRectangle.use_case import AddRectangle
from use_cases.AddRectangle.view import view_factory as view_factory_03
from use_cases.AddText.presenter import presenter_factory as presenter_factory_04
from use_cases.AddText.use_case import AddText
from use_cases.AddText.view import view_factory as view_factory_04
from use_cases_high_level.AddTextBox.presenter import presenter_factory as presenter_factory_01
from use_cases_high_level.AddTextBox.use_case import AddTextBox
from use_cases_high_level.AddTextBox.view import view_factory as view_factory_01


def add_ten_text_boxes(test_app, view):
    presenter = presenter_factory_01()
    presenter.attach(view_factory_01(view))
    for i in range(10):
        command_add = AddTextBox(presenter, test_app.entities)
        command_add.configure(**get_request_model_for_add_text_box(xy_rect=(20, 30 * i),
                                                                   xy_text=(20, 30 * i),
                                                                   text=f'text {i}',
                                                                   tags_rect=(f'text_box_{i}',),
                                                                   tags_text=(f'text_box_{i}',)))
        command_add.execute()


def add_ten_lines(test_app, view):
    presenter = presenter_factory_02()
    presenter.attach(view_factory_02(view))
    for i in range(10):
        command_add = AddLine(presenter, test_app.entities)
        command_add.configure(**get_request_model_for_add_line((10, 10),
                                                               (i * 15 + 10, 200),
                                                               'blue',
                                                               5,
                                                               True,
                                                               (f'line_{i}',),
                                                               ))
        command_add.execute()


def add_ten_rectangles(test_app, view):
    presenter = presenter_factory_03()
    presenter.attach(view_factory_03(view))
    for i in range(10):
        command_add = AddRectangle(presenter, test_app.entities)
        command_add.configure(**get_request_model_for_add_rectangle((40, 10 + i * 30),
                                                                    (10 + i * 30, 20),
                                                                    'red',
                                                                    i,
                                                                    'light green',
                                                                    (f'rect_{i}',),
                                                                    ))
        command_add.execute()


def add_ten_texts(test_app, view):
    presenter = presenter_factory_04()
    presenter.attach(view_factory_04(view))
    for i in range(10):
        command_add = AddText(presenter, test_app.entities)
        command_add.configure(**get_request_model_for_add_text((40, 10 + i * 30),
                                                               f'Text_{i}',
                                                               wh=(10 + i * 30, 20),
                                                               text_rotation=0,
                                                               tags=(f'text_{i}',),
                                                               ))
        command_add.execute()
