import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        from apps.test_app import TestApp
        package_name = 'use_cases.MoveText'
        canvas_color = 'light green'
        test_app = TestApp(package_name, canvas_color)
        view = test_app.view
        command = test_app.use_case_command

        # Controller setting
        # Keyboard setting
        def keyboard_shortcut_handler(modifiers: int, key: str):
            delta_x = 10
            delta_y = 10
            request_model = {'shape_id': f'text_{1}', 'delta_x': 0, 'delta_y': 0}
            if modifiers == 0 and key == 'Left':
                request_model = {'shape_id': f'text_{1}', 'delta_x': -delta_x, 'delta_y': 0}
            elif modifiers == 0 and key == 'Right':
                request_model = {'shape_id': f'text_{1}', 'delta_x': delta_x, 'delta_y': 0}
            elif modifiers == 0 and key == 'Up':
                request_model = {'shape_id': f'text_{1}', 'delta_x': 0, 'delta_y': -delta_y}
            elif modifiers == 0 and key == 'Down':
                request_model = {'shape_id': f'text_{1}', 'delta_x': 0, 'delta_y': delta_y}
            elif modifiers == 8 and key == '1':
                request_model = {'shape_id': f'text_{1}', 'delta_x': delta_x, 'delta_y': delta_y}

            command.configure(**request_model)
            command.execute()

        test_app.set_keyboard_shortcut_handler(keyboard_shortcut_handler)

        # Mouse setting
        def upon_mouse_click(request):
            pass

        def upon_mouse_drag(request):
            r = request
            request_model = {'shape_id': r['shape_id'], 'delta_x': r['delta_x'], 'delta_y': r['delta_y']}
            command.configure(**request_model)
            command.execute()

        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_left_click, {})
        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_shift_left_click, {})
        test_app.configure_mouse(upon_mouse_drag, test_app.mouse.is_left_drag, {'shape_id': f'text_{1}', })
        test_app.configure_mouse(upon_mouse_drag, test_app.mouse.is_shift_left_drag, {'shape_id': f'text_{2}', })

        from Tests.test_methods import add_ten_texts
        add_ten_texts(test_app, view)

        test_app.launch_app()


if __name__ == '__main__':
    unittest.main()
