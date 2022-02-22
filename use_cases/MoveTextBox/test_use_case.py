import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        from apps.test_app import TestApp
        package_name = 'use_cases.MoveTextBox'
        canvas_color = 'pink'
        test_app = TestApp(package_name, canvas_color)
        view = test_app.view
        command = test_app.use_case_command

        # Controller setting
        # Keyboard setting
        from use_cases.MoveRectangle.request_model import get_request_model as get_request_model_01
        from use_cases.MoveText.request_model import get_request_model as get_request_model_02
        def keyboard_shortcut_handler(modifiers: int, key: str):
            n = None
            if modifiers == 8 and key == '1':
                n = 3
            elif modifiers == 8 and key == '2':
                n = 4
            elif modifiers == 8 and key == '3':
                n = 5
            elif modifiers == 8 and key == '4':
                n = 6

            if n is not None:
                request_model = {
                    '1': get_request_model_01(f'text_box_{n}', 20, 20),
                    '2': get_request_model_02(f'text_box_{n}', 20, 20),
                }

                command.configure(**request_model)
                command.execute()

        test_app.set_keyboard_shortcut_handler(keyboard_shortcut_handler)

        # Mouse setting
        def upon_mouse_click(request):
            pass

        def upon_mouse_drag(request):
            request_model = {
                '1': get_request_model_01(f'text_box_{request["n"]}', request['delta_x'] / 2, request['delta_y'] / 2),
                '2': get_request_model_02(f'text_box_{request["n"]}', request['delta_x'] / 2, request['delta_y'] / 2),
            }
            command.configure(**request_model)
            command.execute()

        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_left_click, {})
        test_app.configure_mouse(upon_mouse_drag, test_app.mouse.is_left_drag, {'n': 1})
        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_right_click, {})
        test_app.configure_mouse(upon_mouse_drag, test_app.mouse.is_right_drag, {'n': 2})

        from use_cases.AddTextBox.use_case import AddTextBox
        from use_cases.AddTextBox.presenter import presenter_factory
        from use_cases.AddTextBox.view import view_factory
        from use_cases import get_request_model_for_add_text_box as rm
        presenter = presenter_factory()
        presenter.attach(view_factory(view))
        for i in range(10):
            # Add 10 text boxes
            command_add = AddTextBox(presenter, test_app.entities)
            command_add.configure(**rm(xy_rect=(20, 30 * i), xy_text=(20, 30 * i), text=f'text {i}',
                                       tags_rect=(f'text_box_{i}',), tags_text=(f'text_box_{i}',)))
            command_add.execute()

        test_app.launch_app()


if __name__ == '__main__':
    unittest.main()
