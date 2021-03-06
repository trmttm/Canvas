import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        from apps.test_app import TestApp
        package_name = 'use_cases.AddRectangle'
        canvas_color = 'light yellow'
        test_app = TestApp(package_name, canvas_color)
        view = test_app.view
        command = test_app.use_case_command

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
                command.configure(**request_model)
                command.execute()
            elif key in tuple(str(k) for k in range(9)):
                request_model = {'xy': view.get_mouse_canvas_coordinate(),
                                 'wh': (50, 20),
                                 'border_color': color[int(key)],
                                 'border_width': 1,
                                 'fill': 'light green', }
                command.configure(**request_model)
                command.execute()

        test_app.set_keyboard_shortcut_handler(keyboard_shortcut_handler)

        # Mouse setting

        def upon_mouse_click(request):
            request_model = {'xy': (request['x'], request['y']),
                             'wh': (50, 20),
                             'border_color': 'red',
                             'border_width': 1,
                             'fill': 'light green', }
            command.configure(**request_model)
            command.execute()

        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_left_click, {})
        test_app.launch_app()


if __name__ == '__main__':
    unittest.main()
