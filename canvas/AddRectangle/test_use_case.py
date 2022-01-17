import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        package_name = 'canvas.AddRectangle'
        from importlib import import_module
        color = {
            1: 'black',
            2: 'red',
            3: 'blue',
            4: 'yellow',
            5: 'orange',
            6: 'pink',
            7: 'purple',
        }

        # Choose App/Main
        from app_tkinter import app_tkinter_factory
        app = app_tkinter_factory()

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
            if modifiers == 8 and key == 'a':
                request_model = {'xy': app.get_mouse_canvas_coordinate(),
                                 'wh': (50, 20),
                                 'border_color': 'red',
                                 'border_width': 1,
                                 'fill': 'light green', }
                command = controller_command_factory(presenter, request_model)
                command.execute()
            elif key in tuple(str(k) for k in range(9)):
                request_model = {'xy': app.get_mouse_canvas_coordinate(),
                                 'wh': (50, 20),
                                 'border_color': color[int(key)],
                                 'border_width': 1,
                                 'fill': 'light green', }
                command = controller_command_factory(presenter, request_model)
                command.execute()

        app.set_keyboard_shortcut_handler('root', keyboard_shortcut_handler)

        # Mouse setting
        from mouse import MouseController
        mouse = MouseController()

        def upon_mouse_click(request):
            request_model = {'xy': (request['x'], request['y']),
                             'wh': (50, 20),
                             'border_color': 'red',
                             'border_width': 1,
                             'fill': 'light green', }
            command = controller_command_factory(presenter, request_model)
            command.execute()

        mouse.configure(0, upon_mouse_click, mouse.is_left_click, {})
        app.bind_command_to_widget('canvas1', mouse.handle)

        app.launch_app()


if __name__ == '__main__':
    unittest.main()
