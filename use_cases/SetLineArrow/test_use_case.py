import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        # Choose App/Main
        from app_tkinter import app_tkinter_factory
        app = app_tkinter_factory('orange')

        package_name = 'use_cases.SetLineArrow'
        from importlib import import_module
        # Choose presenter & view
        presenter_factory = import_module(f'{package_name}.presenter', '.').presenter_factory
        view_factory = import_module(f'{package_name}.view', '.').view_factory

        presenter = presenter_factory()
        view = view_factory(app)
        presenter.attach(view)

        # Define controller command
        controller_command_factory = import_module(f'{package_name}.controller', '.').controller_command

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
                command = controller_command_factory(presenter, None)
                command.configure(**request_model)
                command.execute()

        app.set_keyboard_shortcut_handler('root', keyboard_shortcut_handler)

        # Mouse setting
        from mouse import MouseController
        mouse = MouseController()

        def upon_mouse_click(request):
            request_model = {'shape_id': request['shape_id'], 'arrow': request['arrow']}
            command = controller_command_factory(presenter, None)
            command.configure(**request_model)
            command.execute()

        mouse.configure(0, upon_mouse_click, mouse.is_left_click, {'shape_id': (f'line_{5}',), 'arrow': 'start'})
        mouse.configure(1, upon_mouse_click, mouse.is_right_click, {'shape_id': (f'line_{6}',), 'arrow': 'both'})
        app.bind_command_to_widget('canvas1', mouse.handle)

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

            app.add_line(view_model)

        app.launch_app()


if __name__ == '__main__':
    unittest.main()
