import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        from apps.test_app import TestApp
        package_name = 'use_cases.SetLineWidth'
        canvas_color = 'orange'
        test_app = TestApp(package_name, canvas_color)
        view = test_app.view
        command = test_app.use_case_command

        # Controller setting
        # Keyboard setting
        def keyboard_shortcut_handler(modifiers: int, key: str):
            width = None
            if modifiers == 8 and key == '1':
                width = 1
            elif modifiers == 8 and key == '2':
                width = 2
            elif modifiers == 8 and key == '3':
                width = 3
            elif modifiers == 8 and key == '4':
                width = 4

            if width is not None:
                request_model = {'shape_id': f'line_{0}', 'width': width}
                command.configure(**request_model)
                command.execute()

        test_app.set_keyboard_shortcut_handler(keyboard_shortcut_handler)

        # Mouse setting
        def upon_mouse_click(request):
            request_model = {'shape_id': request['shape_id'], 'width': request['width']}
            command.configure(**request_model)
            command.execute()

        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_left_click,
                                 {'shape_id': f'line_{5}', 'width': 1})
        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_right_click,
                                 {'shape_id': f'line_{6}', 'width': 10})

        from Tests.test_methods import add_ten_lines
        add_ten_lines(test_app, view)

        test_app.launch_app()


if __name__ == '__main__':
    unittest.main()
