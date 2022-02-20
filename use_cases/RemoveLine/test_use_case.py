import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        from apps.test_app import TestApp
        package_name = 'use_cases.RemoveLine'
        canvas_color = 'light green'
        test_app = TestApp(package_name, canvas_color)
        view = test_app.view
        presenter = test_app.presenter
        use_case_command = test_app.use_case_command

        # Controller setting
        # Keyboard setting
        def keyboard_shortcut_handler(modifiers: int, key: str):
            if modifiers == 8 and key == '1':
                request_model = {'shape_id': (f'line_{1}',), }
                command = use_case_command(presenter, None)
                command.configure(**request_model)
                command.execute()

        view.set_keyboard_shortcut_handler('root', keyboard_shortcut_handler)

        # Mouse setting
        from mouse import MouseController
        mouse = MouseController()

        def upon_mouse_click(request):
            request_model = {'shape_id': request['shape_id'], }
            command = use_case_command(presenter, None)
            command.configure(**request_model)
            command.execute()

        mouse.configure(0, upon_mouse_click, mouse.is_left_click, {'shape_id': (f'line_{5}',), })
        mouse.configure(1, upon_mouse_click, mouse.is_right_click, {'shape_id': (f'line_{6}',), })
        view.bind_command_to_widget('canvas1', mouse.handle)

        # Add line to delete
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
