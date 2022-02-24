import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        from apps.test_app import TestApp
        package_name = 'use_cases.SelectShapesInRange'
        canvas_color = 'white'
        test_app = TestApp(package_name, canvas_color)
        view = test_app.view
        command = test_app.use_case_command

        # Controller setting
        # Keyboard setting
        from request_models import get_request_model_for_select_shapes_in_range
        get_request_model = get_request_model_for_select_shapes_in_range

        def keyboard_shortcut_handler(modifiers: int, key: str):
            if modifiers == 8 and key == '1':
                request_model = get_request_model('rectangle_0')
                command.configure(**request_model)
                command.update_entities()
                command.present()

        test_app.set_keyboard_shortcut_handler(keyboard_shortcut_handler)

        # Mouse setting
        def upon_mouse_click(request):
            pass

        from use_cases_high_level.MoveTextBox.use_case import MoveTextBox
        from use_cases_high_level.MoveTextBox.presenter import presenter_factory
        from use_cases_high_level.MoveTextBox.view import view_factory
        from request_models import get_request_model_for_move_text_box
        presenter = presenter_factory()
        presenter.attach(view_factory(view))
        move_text_box = MoveTextBox(presenter, test_app.entities)

        def upon_mouse_drag(request):
            request_model = get_request_model_for_move_text_box('rectangle_1',
                                                                'text_0',
                                                                request['delta_x'],
                                                                request['delta_y'])
            move_text_box.configure(**request_model)
            move_text_box.execute()

            command.configure(**get_request_model('rectangle_0'))
            command.execute()

            selected_shape_ids = test_app.entities.group.get_contents('selected_shapes')
            r = 'rectangle_1'
            if r in selected_shape_ids:
                print(f'{r} is selected!')
            r = 'text_0'
            if r in selected_shape_ids:
                print(f'{r} is selected!\n')

        from use_cases.MoveLine.use_case import MoveLine
        from use_cases.MoveLine.presenter import presenter_factory
        from use_cases.MoveLine.view import view_factory
        from request_models import get_request_model_for_move_line
        presenter = presenter_factory()
        presenter.attach(view_factory(view))
        move_line = MoveLine(presenter, test_app.entities)

        def upon_mouse_drag2(request):
            x1, y1 = test_app.entities.lines.get_xy1('line_0')
            x2, y2 = test_app.entities.lines.get_xy2('line_0')
            coordinates_from = x1 + request['delta_x'], y1 + request['delta_y']
            coordinates_to = x2 + request['delta_x'], y2 + request['delta_y']
            request_model = get_request_model_for_move_line('line_0',
                                                            coordinates_from,
                                                            coordinates_to,
                                                            )
            move_line.configure(**request_model)
            move_line.execute()

            command.configure(**get_request_model('rectangle_0'))
            command.execute()

            selected_shape_ids = test_app.entities.group.get_contents('selected_shapes')
            r = 'line_0'
            if r in selected_shape_ids:
                print(f'{r} is selected!')

        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_left_click, {})
        test_app.configure_mouse(upon_mouse_drag, test_app.mouse.is_left_drag, {})
        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_shift_left_click, {})
        test_app.configure_mouse(upon_mouse_drag2, test_app.mouse.is_shift_left_drag, {})

        # Selector Rectangle
        from use_cases.AddRectangle.use_case import AddRectangle
        from use_cases.AddRectangle.presenter import presenter_factory
        from use_cases.AddRectangle.view import view_factory
        presenter = presenter_factory()
        presenter.attach(view_factory(view))
        add_rectangle = AddRectangle(presenter, test_app.entities)
        add_rectangle.configure((40, 40), (400, 400), tags=('selector',))
        add_rectangle.execute()

        # TextBox to move around
        from use_cases_high_level.AddTextBox.use_case import AddTextBox
        from use_cases_high_level.AddTextBox.presenter import presenter_factory
        from use_cases_high_level.AddTextBox.view import view_factory
        from request_models import get_request_model_for_add_text_box as rm
        presenter = presenter_factory()
        presenter.attach(view_factory(view))
        add_text_box = AddTextBox(presenter, test_app.entities)
        add_text_box.configure(
            **rm((20, 20), (100, 20), xy_text=(20, 20), wh_text=(100, 20), tags_rect=('tb',), tags_text=('tb',)))
        add_text_box.execute()

        # Line to move around
        from use_cases.AddLine.use_case import AddLine
        from use_cases.AddLine.presenter import presenter_factory
        from use_cases.AddLine.view import view_factory
        from request_models import get_request_model_for_add_line as rm
        presenter = presenter_factory()
        presenter.attach(view_factory(view))
        add_line = AddLine(presenter, test_app.entities)
        add_line.configure(**rm((30, 30), (100, 100)))
        add_line.execute()

        # User Feedback
        from use_cases.AddText.use_case import AddText
        from use_cases.AddText.presenter import presenter_factory
        from use_cases.AddText.view import view_factory
        presenter = presenter_factory()
        presenter.attach(view_factory(view))
        add_text = AddText(presenter, test_app.entities)
        add_text.configure((40, 400), 'Selection = ', wh=(200, 20), tags=('selector',))
        add_text.execute()

        test_app.launch_app()


if __name__ == '__main__':
    unittest.main()
