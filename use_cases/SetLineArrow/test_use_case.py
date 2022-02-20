import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        from apps.test_app import TestApp
        package_name = 'use_cases.SetLineArrow'
        canvas_color = 'orange'
        test_app = TestApp(package_name, canvas_color)
        view = test_app.view
        presenter = test_app.presenter
        use_case_command = test_app.use_case_command

        # Controller setting
        # Keyboard setting
        def keyboard_shortcut_handler(modifiers: int, key: str):
            arrow = 'None'
            if modifiers == 8 and key == '1':
                arrow = 'start'
            elif modifiers == 8 and key == '2':
                arrow = 'end'
            elif modifiers == 8 and key == '3':
                arrow = 'both'
            elif modifiers == 8 and key == '4':
                arrow = None

            if arrow != 'None':
                request_model = {'shape_id': (f'line_{0}',), 'arrow': arrow}
                command = use_case_command(presenter, None)
                command.configure(**request_model)
                command.execute()

        test_app.set_keyboard_shortcut_handler(keyboard_shortcut_handler)

        # Mouse setting
        def upon_mouse_click(request):
            request_model = {'shape_id': request['shape_id'], 'arrow': request['arrow']}
            command = use_case_command(presenter, None)
            command.configure(**request_model)
            command.execute()

        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_left_click,
                                 {'shape_id': (f'line_{5}',), 'arrow': 'start'})
        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_right_click,
                                 {'shape_id': (f'line_{6}',), 'arrow': 'both'})

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
