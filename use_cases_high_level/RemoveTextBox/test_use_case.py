import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        from apps.test_app import TestApp
        package_name = 'use_cases_high_level.RemoveTextBox'
        canvas_color = 'light yellow'
        test_app = TestApp(package_name, canvas_color)
        view = test_app.view
        command = test_app.use_case_command

        # Controller setting
        # Keyboard setting
        from use_cases.RemoveRectangle.request_model import get_request_model as get_request_model_01
        from use_cases.RemoveText.request_model import get_request_model as get_request_model_02
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
                    '1': get_request_model_01(f'text_box_{n}'),
                    '2': get_request_model_02(f'text_box_{n}'),
                }

                command.configure(**request_model)
                command.execute()

        test_app.set_keyboard_shortcut_handler(keyboard_shortcut_handler)

        # Mouse setting
        def upon_mouse_click(request):
            request_model = {
                '1': get_request_model_01(f'text_box_{request["n"]}'),
                '2': get_request_model_02(f'text_box_{request["n"]}'),
            }
            command.configure(**request_model)
            command.execute()

        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_left_click, {'n': 1})
        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_right_click, {'n': 2})

        from Tests.test_methods import add_ten_text_boxes
        add_ten_text_boxes(test_app, view)

        test_app.launch_app()


if __name__ == '__main__':
    unittest.main()
