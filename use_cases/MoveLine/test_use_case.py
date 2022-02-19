import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        # Choose App/Main
        from app_tkinter import app_tkinter_factory
        app = app_tkinter_factory('light green')

        package_name = 'use_cases.MoveLine'
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
            request_model = None
            if modifiers == 8 and key == '1':
                request_model = {'shape_id': (f'line_{0}',), 'coordinates_from': (100, 50), 'coordinates_to': (300, 50)}
            elif modifiers == 8 and key == '2':
                request_model = {'shape_id': (f'line_{1}',), 'coordinates_from': (100, 60), 'coordinates_to': (300, 60)}
            elif modifiers == 8 and key == '3':
                request_model = {'shape_id': (f'line_{3}',), 'coordinates_from': (100, 70), 'coordinates_to': (300, 70)}

            if request_model is not None:
                command = controller_command_factory(presenter, None)
                command.configure(**request_model)
                command.execute()

        app.set_keyboard_shortcut_handler('root', keyboard_shortcut_handler)

        # Mouse setting
        from mouse import MouseController
        mouse = MouseController()

        def upon_mouse_click(request):
            pass

        def upon_mouse_drag(request):
            shape_id = request.get('shape_id', None)
            if shape_id is not None:
                x, y = request['x'], request['y']
                request_model = {'shape_id': shape_id, 'coordinates_from': (20, 20), 'coordinates_to': (x, y)}
                command = controller_command_factory(presenter, None)
                command.configure(**request_model)
                command.execute()

        mouse.configure(0, upon_mouse_click, mouse.is_left_click, {})
        mouse.configure(2, upon_mouse_drag, mouse.is_left_drag, {'shape_id': (f'line_{1}',), })
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
