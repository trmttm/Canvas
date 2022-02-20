import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        from apps.test_app import TestApp
        package_name = 'use_cases.AddRectangle'
        canvas_color = 'light yellow'
        test_app = TestApp(package_name, canvas_color)
        view = test_app.view
        presenter = test_app.presenter
        use_case_command = test_app.use_case_command

        color = {
            1: 'black',
            2: 'red',
            3: 'blue',
            4: 'yellow',
            5: 'orange',
            6: 'pink',
            7: 'purple',
        }

        # Controller setting
        # Keyboard setting
        def keyboard_shortcut_handler(modifiers: int, key: str):
            if modifiers == 8 and key == 'a':
                request_model = {'xy': view.get_mouse_canvas_coordinate(),
                                 'wh': (50, 20),
                                 'border_color': 'red',
                                 'border_width': 1,
                                 'fill': 'light green', }
                command = use_case_command(presenter, None)
                command.configure(**request_model)
                command.execute()
            elif key in tuple(str(k) for k in range(9)):
                request_model = {'xy': view.get_mouse_canvas_coordinate(),
                                 'wh': (50, 20),
                                 'border_color': color[int(key)],
                                 'border_width': 1,
                                 'fill': 'light green', }
                command = use_case_command(presenter, None)
                command.configure(**request_model)
                command.execute()

        view.set_keyboard_shortcut_handler('root', keyboard_shortcut_handler)

        # Mouse setting
        from mouse import MouseController
        mouse = MouseController()

        def upon_mouse_click(request):
            request_model = {'xy': (request['x'], request['y']),
                             'wh': (50, 20),
                             'border_color': 'red',
                             'border_width': 1,
                             'fill': 'light green', }
            command = use_case_command(presenter, None)
            command.configure(**request_model)
            command.execute()

        mouse.configure(0, upon_mouse_click, mouse.is_left_click, {})
        view.bind_command_to_widget('canvas1', mouse.handle)

        view.launch_app()


if __name__ == '__main__':
    unittest.main()
