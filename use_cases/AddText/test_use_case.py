import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        package_name = 'use_cases.AddText'
        from importlib import import_module
        # Choose App/Main
        from app_tkinter import app_tkinter_factory
        app = app_tkinter_factory('white')

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
            if modifiers == 8 and key == '1':
                request_model = {'xy': app.get_mouse_canvas_coordinate(),
                                 'text': 'New Text!',
                                 'tags': (f'text_1',), }
                command = controller_command_factory(presenter, request_model)
                command.update_entities()

        app.set_keyboard_shortcut_handler('root', keyboard_shortcut_handler)

        # Mouse setting
        from mouse import MouseController
        mouse = MouseController()

        def upon_mouse_click(request):
            request_model = {'xy': (request['x'], request['y']),
                             'text': 'New Text by mouse!',
                             'tabs': 'text_1', }
            command = controller_command_factory(presenter, request_model)
            command.update_entities()

        mouse.configure(0, upon_mouse_click, mouse.is_left_click, {})
        app.bind_command_to_widget('canvas1', mouse.handle)

        app.launch_app()


if __name__ == '__main__':
    unittest.main()
