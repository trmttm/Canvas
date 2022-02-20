import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        package_name = 'use_cases.AddTextBox'
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
        from use_cases.AddRectangle.request_model import get_request_model as get_request_model_01
        from use_cases.AddText.request_model import get_request_model as get_request_model_02
        def keyboard_shortcut_handler(modifiers: int, key: str):
            if modifiers == 8 and key == '1':
                request_model = {
                    '1': get_request_model_01(app.get_mouse_canvas_coordinate(), (50, 20), 'red', 1, 'light green',
                                              'rect_01'),
                    '2': get_request_model_02(app.get_mouse_canvas_coordinate(), 'New Text!', tags=('text_01',)),
                }
                command = controller_command_factory(presenter, None)
                command.configure(**request_model)
                command.execute()

        app.set_keyboard_shortcut_handler('root', keyboard_shortcut_handler)

        # Mouse setting
        from mouse import MouseController
        mouse = MouseController()

        def upon_mouse_click(request):
            request_model = {'xy': (request['x'], request['y']),
                             'text': 'New Text by mouse!',
                             'tags': 'text_1', }
            command = controller_command_factory(presenter, None)
            command.configure(**request_model)
            command.execute()

        mouse.configure(0, upon_mouse_click, mouse.is_left_click, {})
        app.bind_command_to_widget('canvas1', mouse.handle)

        app.launch_app()


if __name__ == '__main__':
    unittest.main()
