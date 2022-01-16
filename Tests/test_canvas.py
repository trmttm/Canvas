import unittest


class MyTestCase(unittest.TestCase):
    def test_integrating_multiple_use_cases(self):
        # Choose App/Main
        from app_tkinter import app_tkinter_factory
        app = app_tkinter_factory('pink')

        no_modifier = 0
        modifier_add = 8
        modifier_option = 16

        # (modifier, key): request_model
        keyboard_shortcut_map = {
            (modifier_add, '0'): {
                'xy': (40, 10),
                'wh': (50, 20),
                'border_color': 'red',
                'border_width': 1,
                'fill': 'light green',
                'tags': ('rect_0',),
                'package_number': 0,
            },
            (modifier_add, '1'): {
                'xy': (40, 40),
                'wh': (50, 20),
                'border_color': 'green',
                'border_width': 1,
                'fill': 'light green',
                'tags': ('rect_1',),
                'package_number': 0,
            },
            (modifier_add, '2'): {
                'xy': (40, 70),
                'wh': (50, 20),
                'border_color': 'blue',
                'border_width': 1,
                'fill': 'light green',
                'tags': ('rect_2',),
                'package_number': 0,
            },
            (modifier_add, '3'): {
                'xy': (40, 100),
                'wh': (50, 20),
                'border_color': 'yellow',
                'border_width': 1,
                'fill': 'light green',
                'tags': ('rect_3',),
                'package_number': 0,
            },
            (modifier_add, '4'): {
                'xy': (40, 130),
                'wh': (50, 20),
                'border_color': 'orange',
                'border_width': 1,
                'fill': 'light green',
                'tags': ('rect_4',),
                'package_number': 0,
            },
            (modifier_add, '5'): {
                'xy': (40, 170),
                'wh': (50, 20),
                'border_color': 'pink',
                'border_width': 1,
                'fill': 'light green',
                'tags': ('rect_5',),
                'package_number': 0,
            },
            (modifier_option, '0'): {'shape_id': 'rect_0', 'package_number': 1},
            (modifier_option, '1'): {'shape_id': 'rect_1', 'package_number': 1},
            (modifier_option, '2'): {'shape_id': 'rect_2', 'package_number': 1},
            (modifier_option, '3'): {'shape_id': 'rect_3', 'package_number': 1},
            (modifier_option, '4'): {'shape_id': 'rect_4', 'package_number': 1},
            (modifier_option, '5'): {'shape_id': 'rect_5', 'package_number': 1},
            (no_modifier, 'Left'): {
                'shape_id': 'rect_0',
                'delta_x': -10,
                'delta_y': 0,
                'package_number': 2
            },
            (no_modifier, 'Right'): {
                'shape_id': 'rect_0',
                'delta_x': 10,
                'delta_y': 0,
                'package_number': 2
            },
            (no_modifier, 'Up'): {
                'shape_id': 'rect_0',
                'delta_x': 0,
                'delta_y': -10,
                'package_number': 2
            },
            (no_modifier, 'Down'): {
                'shape_id': 'rect_0',
                'delta_x': 0,
                'delta_y': 10,
                'package_number': 2
            },
            (no_modifier, '1'): {'shape_id': 'rect_1', 'color': 'red', 'package_number': 3},
            (no_modifier, '2'): {'shape_id': 'rect_1', 'color': 'green', 'package_number': 3},
            (no_modifier, '3'): {'shape_id': 'rect_1', 'color': 'blue', 'package_number': 3},
            (no_modifier, '4'): {'shape_id': 'rect_1', 'width': 1, 'package_number': 4},
            (no_modifier, '5'): {'shape_id': 'rect_1', 'width': 3, 'package_number': 4},
            (no_modifier, '6'): {'shape_id': 'rect_1', 'width': 5, 'package_number': 4},
        }

        package_names = ['AddRectangle', 'RemoveRectangle', 'MoveRectangle', 'SetFillColor', 'SetBorderWidth']
        commands = []
        presenters = []
        views = []
        for package_number, package_name in enumerate(package_names):
            from importlib import import_module
            # Choose presenter & view
            presenter_factory = import_module(f'{package_name}.presenter', '.').presenter_factory
            view_factory = import_module(f'{package_name}.view', '.').view_factory

            presenters.append(presenter_factory())
            views.append(view_factory(app))
            presenter = presenters[package_number]
            view = views[package_number]
            presenter.attach(view)

            # Define controller command
            controller_command = import_module(f'{package_name}.controller', '.').controller_command
            commands.append(controller_command)

        # Controller setting
        # Keyboard setting
        def keyboard_shortcut_handler(modifiers: int, key: str):
            request_model = keyboard_shortcut_map.get((modifiers, key), None)
            if request_model is not None:
                n = request_model.get('package_number')
                command = commands[n]
                presenter_ = presenters[n]
                command(presenter_, request_model)

        app.set_keyboard_shortcut_handler('root', keyboard_shortcut_handler)

        # Mouse setting
        from mouse import MouseController
        mouse = MouseController()

        def upon_mouse_click(request, ):
            command = request['command']
            if command is not None:
                command(presenter, request)

        mouse.configure(0, upon_mouse_click, mouse.is_left_click, {'shape_id': (f'rect_{1}',),
                                                                   'command': None,
                                                                   })
        mouse.configure(1, upon_mouse_click, mouse.is_left_drag, {'shape_id': (f'rect_{1}',),
                                                                  'command': commands[2],
                                                                  })
        app.bind_command_to_widget('canvas1', mouse.handle)

        app.launch_app()


if __name__ == '__main__':
    unittest.main()
