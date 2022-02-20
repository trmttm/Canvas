import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        from apps.test_app import TestApp
        package_name = 'use_cases.SetBorderWidth'
        canvas_color = 'light green'
        test_app = TestApp(package_name, canvas_color)
        view = test_app.view
        presenter = test_app.presenter
        use_case_command = test_app.use_case_command

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
                request_model = {'shape_id': (f'rect_{8}',), 'width': width}
                command = use_case_command(presenter, None)
                command.configure(**request_model)
                command.execute()

        test_app.set_keyboard_shortcut_handler(keyboard_shortcut_handler)

        # Mouse setting
        def upon_mouse_click(request):
            request_model = {'shape_id': request['shape_id'], 'width': request['width']}
            command = use_case_command(presenter, None)
            command.configure(**request_model)
            command.execute()

        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_left_click,
                                 {'shape_id': (f'rect_{5}',), 'width': 1})
        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_right_click,
                                 {'shape_id': (f'rect_{6}',), 'width': 10})

        # Add rectangles to delete
        for i in range(10):
            view_model = {'x': 40,
                          'y': 10 + i * 30,
                          'width': 10 + i * 30,
                          'height': 20,
                          'border_color': 'red',
                          'border_width': i,
                          'fill': 'light green',
                          'tags': (f'rect_{i}',)
                          }

            view.add_rectangle(view_model)

        test_app.launch_app()


if __name__ == '__main__':
    unittest.main()
