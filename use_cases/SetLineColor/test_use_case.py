import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        from apps.test_app import TestApp
        package_name = 'use_cases.SetLineColor'
        canvas_color = 'grey'
        test_app = TestApp(package_name, canvas_color)
        view = test_app.view
        command = test_app.use_case_command

        # Controller setting
        # Keyboard setting
        def keyboard_shortcut_handler(modifiers: int, key: str):
            color = None
            if modifiers == 8 and key == '1':
                color = 'red'
            elif modifiers == 8 and key == '2':
                color = 'green'
            elif modifiers == 8 and key == '3':
                color = 'blue'
            elif modifiers == 8 and key == '4':
                color = 'yellow'

            if color is not None:
                request_model = {'shape_id': (f'line_{8}',), 'color': color}
                command.configure(**request_model)
                command.execute()

        test_app.set_keyboard_shortcut_handler(keyboard_shortcut_handler)

        # Mouse setting
        def upon_mouse_click(request):
            request_model = {'shape_id': request['shape_id'], 'color': request['color']}
            command.configure(**request_model)
            command.execute()

        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_left_click,
                                 {'shape_id': (f'line_{5}',), 'color': 'green'})
        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_right_click,
                                 {'shape_id': (f'line_{6}',), 'color': 'yellow'})

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

        test_app.launch_app()


if __name__ == '__main__':
    unittest.main()
