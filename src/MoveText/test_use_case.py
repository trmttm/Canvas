import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        # Choose App/Main
        from app_tkinter import app_tkinter_factory
        app = app_tkinter_factory('light green')

        package_name = 'src.MoveText'
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
            delta_x = 10
            delta_y = 10
            request_model = {'shape_id': (f'rect_{1}',), 'delta_x': 0, 'delta_y': 0}
            if modifiers == 0 and key == 'Left':
                request_model = {'shape_id': (f'rect_{1}',), 'delta_x': -delta_x, 'delta_y': 0}
            elif modifiers == 0 and key == 'Right':
                request_model = {'shape_id': (f'rect_{1}',), 'delta_x': delta_x, 'delta_y': 0}
            elif modifiers == 0 and key == 'Up':
                request_model = {'shape_id': (f'rect_{1}',), 'delta_x': 0, 'delta_y': -delta_y}
            elif modifiers == 0 and key == 'Down':
                request_model = {'shape_id': (f'rect_{1}',), 'delta_x': 0, 'delta_y': delta_y}
            elif modifiers == 8 and key == '1':
                request_model = {'shape_id': (f'rect_{1}',), 'delta_x': delta_x, 'delta_y': delta_y}

            command = controller_command_factory(presenter, request_model)
            command.execute()

        app.set_keyboard_shortcut_handler('root', keyboard_shortcut_handler)

        # Mouse setting
        from mouse import MouseController
        mouse = MouseController()

        def upon_mouse_click(request):
            pass

        def upon_mouse_drag(request):
            r = request
            request_model = {'shape_id': r['shape_id'], 'delta_x': r['delta_x'], 'delta_y': r['delta_y']}
            command = controller_command_factory(presenter, request_model)
            command.execute()

        mouse.configure(0, upon_mouse_click, mouse.is_left_click, {})
        mouse.configure(1, upon_mouse_click, mouse.is_shift_left_click, {})
        mouse.configure(2, upon_mouse_drag, mouse.is_left_drag, {'shape_id': (f'rect_{1}',), })
        mouse.configure(3, upon_mouse_drag, mouse.is_shift_left_drag, {'shape_id': (f'rect_{2}',), })
        app.bind_command_to_widget('canvas1', mouse.handle)

        # Add rectangles to delete
        for i in range(10):
            view_model = {'x': 40,
                          'y': 10 + i * 30,
                          'width': 100,
                          'height': 20,
                          'text_rotation': 0,
                          'text': f'Move this text {i}',
                          'tags': (f'rect_{i}',)
                          }

            app.add_text(view_model)

        app.launch_app()


if __name__ == '__main__':
    unittest.main()
