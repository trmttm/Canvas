import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        # Choose App/Main
        from app_tkinter import app_tkinter_factory
        app = app_tkinter_factory('yellow')

        package_name = 'SetFillColor'
        from importlib import import_module
        # Choose presenter & view
        presenter_factory = import_module(f'{package_name}.presenter', '.').presenter_factory
        view_factory = import_module(f'{package_name}.view', '.').view_factory

        presenter = presenter_factory()
        view = view_factory(app)
        presenter.attach(view)

        # Define controller command
        controller_command = import_module(f'{package_name}.controller', '.').controller_command

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
                request_model = {'shape_id': (f'rect_{8}',), 'color': color}
                controller_command(presenter, request_model)

        app.set_keyboard_shortcut_handler('root', keyboard_shortcut_handler)

        # Mouse setting
        from mouse import MouseController
        mouse = MouseController()

        def upon_mouse_click(request):
            request_model = {'shape_id': request['shape_id'], }
            controller_command(presenter, request_model)

        mouse.configure(0, upon_mouse_click, mouse.is_left_click, {'shape_id': (f'rect_{5}',), })
        mouse.configure(1, upon_mouse_click, mouse.is_right_click, {'shape_id': (f'rect_{6}',), })
        app.bind_command_to_widget('canvas1', mouse.handle)

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

            app.add_rectangle(view_model)

        app.launch_app()


if __name__ == '__main__':
    unittest.main()
