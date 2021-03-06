import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        from apps.test_app import TestApp
        package_name = 'use_cases.ChangeRectangleShape'
        canvas_color = 'light green'
        test_app = TestApp(package_name, canvas_color)
        view = test_app.view
        command = test_app.use_case_command

        # Controller setting
        # Keyboard setting
        def keyboard_shortcut_handler(modifiers: int, key: str):
            request_model = None
            if modifiers == 8 and key == '1':
                request_model = {'shape_id': f'rect_{0}', 'coordinates_from': (10, 50), 'coordinates_to': (99, 150)}
            elif modifiers == 8 and key == '2':
                request_model = {'shape_id': f'rect_{1}', 'coordinates_from': (10, 60), 'coordinates_to': (99, 160)}
            elif modifiers == 8 and key == '3':
                request_model = {'shape_id': f'rect_{3}', 'coordinates_from': (10, 70), 'coordinates_to': (99, 170)}

            if request_model is not None:
                command.configure(**request_model)
                command.execute()

        test_app.set_keyboard_shortcut_handler(keyboard_shortcut_handler)

        # Mouse setting
        def upon_mouse_click(request):
            pass

        def upon_mouse_drag(request):
            shape_id = request.get('shape_id', None)
            if shape_id is not None:
                x, y = request['x'], request['y']
                x0, y0 = request['coordinates'][0]
                request_model = {'shape_id': shape_id, 'coordinates_from': (x0, y0), 'coordinates_to': (x, y)}
                command.configure(**request_model)
                command.execute()

        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_left_click, {'save click coordinate': True})
        test_app.configure_mouse(upon_mouse_drag, test_app.mouse.is_left_drag, {'shape_id': f'rect_{1}', })

        from Tests.test_methods import add_ten_rectangles
        add_ten_rectangles(test_app, view)

        test_app.launch_app()


if __name__ == '__main__':
    unittest.main()
