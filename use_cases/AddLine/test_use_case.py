import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        from apps.test_app import TestApp
        package_name = 'use_cases.AddLine'
        canvas_color = 'white'
        test_app = TestApp(package_name, canvas_color)
        view = test_app.view
        presenter = test_app.presenter
        use_case_command = test_app.use_case_command

        # Controller setting
        # Keyboard setting
        def keyboard_shortcut_handler(modifiers: int, key: str):
            if modifiers == 8 and key == '1':
                request_model = {'xy1': (10, 10),
                                 'xy2': view.get_mouse_canvas_coordinate(),
                                 'width': 3,
                                 'color': 'red',
                                 'arrow_at_end': True,
                                 'tags': ('line_1',),
                                 }
                command = use_case_command(presenter, None)
                command.configure(**request_model)
                command.update_entities()
                command.present()

        view.set_keyboard_shortcut_handler('root', keyboard_shortcut_handler)

        # Mouse setting
        from mouse import MouseController
        mouse = MouseController()

        def upon_mouse_click(request):
            request_model = {'xy1': (10, 10),
                             'xy2': view.get_mouse_canvas_coordinate(),
                             'width': 5,
                             'color': 'blue',
                             'arrow_at_end': True,
                             'tags': ('line_1',),
                             }
            command = use_case_command(presenter, None)
            command.configure(**request_model)
            # command.update_entities()
            # command.present()
            command.execute()

        mouse.configure(0, upon_mouse_click, mouse.is_left_click, {})
        view.bind_command_to_widget('canvas1', mouse.handle)

        view.launch_app()


if __name__ == '__main__':
    unittest.main()
