import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        from apps.test_app import TestApp
        package_name = 'use_cases.MoveLine'
        canvas_color = 'light green'
        test_app = TestApp(package_name, canvas_color)
        view = test_app.view
        command = test_app.use_case_command

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
                request_model = {'shape_id': shape_id, 'coordinates_from': (20, 20), 'coordinates_to': (x, y)}
                command.configure(**request_model)
                command.execute()

        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_left_click, {})
        test_app.configure_mouse(upon_mouse_drag, test_app.mouse.is_left_drag, {'shape_id': (f'line_{1}',), })

        # Add rectangles
        from use_cases.AddLine.use_case import AddLine
        from use_cases.AddLine.presenter import presenter_factory
        presenter = presenter_factory()
        presenter.attach(view.add_line)
        for i in range(10):
            command_add = AddLine(presenter, test_app.entities)
            command_add.configure((40, 10), (i * 15 + 10, 200), 'blue', 5, True, (f'line_{i}',))
            command_add.execute()

        test_app.launch_app()


if __name__ == '__main__':
    unittest.main()
