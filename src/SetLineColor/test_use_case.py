import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        # Choose App/Main
        from app_tkinter import app_tkinter_factory
        app = app_tkinter_factory('grey')

        package_name = 'src.SetLineColor'
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
                command = controller_command_factory(presenter, request_model)
                command.execute()

        app.set_keyboard_shortcut_handler('root', keyboard_shortcut_handler)

        # Mouse setting
        from mouse import MouseController
        mouse = MouseController()

        def upon_mouse_click(request):
            request_model = {'shape_id': request['shape_id'], }
            command = controller_command_factory(presenter, request_model)
            command.execute()

        mouse.configure(0, upon_mouse_click, mouse.is_left_click, {'shape_id': (f'text_{5}',), })
        mouse.configure(1, upon_mouse_click, mouse.is_right_click, {'shape_id': (f'text_{6}',), })
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
