import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        from apps.test_app import TestApp
        package_name = 'use_cases.SetTextValue'
        canvas_color = 'grey'
        test_app = TestApp(package_name, canvas_color)
        view = test_app.view
        command = test_app.use_case_command

        # Controller setting
        # Keyboard setting
        def keyboard_shortcut_handler(modifiers: int, key: str):
            text = None
            if modifiers == 8 and key == '1':
                text = 'red'
            elif modifiers == 8 and key == '2':
                text = 'green'
            elif modifiers == 8 and key == '3':
                text = 'blue'
            elif modifiers == 8 and key == '4':
                text = 'yellow'

            if text is not None:
                request_model = {'shape_id': f'text_{8}', 'text': text}
                command.configure(**request_model)
                command.execute()

        test_app.set_keyboard_shortcut_handler(keyboard_shortcut_handler)

        # Mouse setting
        def upon_mouse_click(request):
            request_model = {'shape_id': request['shape_id'], 'text': request['text']}
            command.configure(**request_model)
            command.execute()

        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_left_click,
                                 {'shape_id': f'text_{5}', 'text': 'blue'})
        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_right_click,
                                 {'shape_id': f'text_{6}', 'text': 'orange'})

        from Tests.test_methods import add_ten_texts
        add_ten_texts(test_app, view)

        test_app.launch_app()


if __name__ == '__main__':
    unittest.main()
