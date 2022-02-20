import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        from apps.test_app import TestApp
        package_name = 'use_cases.MoveLine'
        canvas_color = 'light green'
        test_app = TestApp(package_name, canvas_color)
        view = test_app.view
        presenter = test_app.presenter
        use_case_command = test_app.use_case_command

        # Controller setting
        # Keyboard setting
        def keyboard_shortcut_handler(modifiers: int, key: str):
            request_model = None
            if modifiers == 8 and key == '1':
                request_model = {'shape_id': (f'line_{0}',), 'coordinates_from': (100, 50), 'coordinates_to': (300, 50)}
            elif modifiers == 8 and key == '2':
                request_model = {'shape_id': (f'line_{1}',), 'coordinates_from': (100, 60), 'coordinates_to': (300, 60)}
            elif modifiers == 8 and key == '3':
                request_model = {'shape_id': (f'line_{3}',), 'coordinates_from': (100, 70), 'coordinates_to': (300, 70)}

            if request_model is not None:
                command = use_case_command(presenter, None)
                command.configure(**request_model)
                command.execute()

        view.set_keyboard_shortcut_handler('root', keyboard_shortcut_handler)

        # Mouse setting
        from mouse import MouseController
        mouse = MouseController()

        def upon_mouse_click(request):
            pass

        def upon_mouse_drag(request):
            shape_id = request.get('shape_id', None)
            if shape_id is not None:
                x, y = request['x'], request['y']
                request_model = {'shape_id': shape_id, 'coordinates_from': (20, 20), 'coordinates_to': (x, y)}
                command = use_case_command(presenter, None)
                command.configure(**request_model)
                command.execute()

        mouse.configure(0, upon_mouse_click, mouse.is_left_click, {})
        mouse.configure(2, upon_mouse_drag, mouse.is_left_drag, {'shape_id': (f'line_{1}',), })
        view.bind_command_to_widget('canvas1', mouse.handle)

        # Add line
        for i in range(10):
            view_model = {
                'line_1': {'coordinate_from': (10, 10),
                           'coordinate_to': (i * 15 + 10, 200),
                           'line_width': 5,
                           'line_color': 'blue',
                           'arrow_at_star': True,
                           'tags': (f'line_{i}',),
                           }
            }

            view.add_line(view_model)

        view.launch_app()


if __name__ == '__main__':
    unittest.main()
