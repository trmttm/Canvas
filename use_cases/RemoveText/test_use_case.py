import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        from apps.test_app import TestApp
        package_name = 'use_cases.RemoveText'
        canvas_color = 'light green'
        test_app = TestApp(package_name, canvas_color)
        view = test_app.view
        presenter = test_app.presenter
        use_case_command = test_app.use_case_command

        # Controller setting
        # Keyboard setting
        def keyboard_shortcut_handler(modifiers: int, key: str):
            if modifiers == 8 and key == '1':
                request_model = {'shape_id': (f'text_{1}',), }
                command = use_case_command(presenter, None)
                command.configure(**request_model)
                command.execute()
            if key in tuple(str(i) for i in range(10)):
                request_model = {'shape_id': (f'text_{key}',), }
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

        mouse.configure(0, upon_mouse_click, mouse.is_left_click, {'shape_id': (f'text_{5}',), })
        mouse.configure(1, upon_mouse_click, mouse.is_right_click, {'shape_id': (f'text_{6}',), })
        view.bind_command_to_widget('canvas1', mouse.handle)

        # Add rectangles to delete
        for i in range(10):
            view_model = {'x': 40,
                          'y': 10 + i * 30,
                          'width': 100,
                          'height': 20,
                          'text_rotation': 0,
                          'text': f'Remove this text{i}',
                          'fill': 'light green',
                          'tags': (f'text_{i}',)
                          }

            view.add_text(view_model)

        view.launch_app()


if __name__ == '__main__':
    unittest.main()
