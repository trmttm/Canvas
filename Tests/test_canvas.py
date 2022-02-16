import unittest


class MyTestCase(unittest.TestCase):
    def test_integrating_basic_use_cases(self):
        # Choose App/Main
        from app_tkinter import app_tkinter_factory
        app = app_tkinter_factory('pink')

        no_modifier = 0
        modifier_command = 8
        modifier_option = 16

        # (modifier, key): request_model
        keyboard_shortcut_map = {
            (modifier_command, '0'): {
                'xy': (40, 10),
                'wh': (50, 20),
                'border_color': 'red',
                'border_width': 1,
                'fill': 'light green',
                'tags': ('rect_0',),
                'package_number': 0,
            },
            (modifier_command, '1'): {
                'xy': (40, 40),
                'wh': (50, 20),
                'border_color': 'green',
                'border_width': 1,
                'fill': 'light green',
                'tags': ('rect_1',),
                'package_number': 0,
            },
            (modifier_command, '2'): {
                'xy': (40, 70),
                'wh': (50, 20),
                'border_color': 'blue',
                'border_width': 1,
                'fill': 'light green',
                'tags': ('rect_2',),
                'package_number': 0,
            },
            (modifier_command, '3'): {
                'xy': (40, 100),
                'wh': (50, 20),
                'border_color': 'yellow',
                'border_width': 1,
                'fill': 'light green',
                'tags': ('rect_3',),
                'package_number': 0,
            },
            (modifier_command, '4'): {
                'xy': (40, 130),
                'wh': (50, 20),
                'border_color': 'orange',
                'border_width': 1,
                'fill': 'light green',
                'tags': ('rect_4',),
                'package_number': 0,
            },
            (modifier_command, '5'): {
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
            (no_modifier, '7'): {'shape_id': 'rect_1', 'color': 'red', 'package_number': 5},
            (no_modifier, '8'): {'shape_id': 'rect_1', 'color': 'green', 'package_number': 5},
            (no_modifier, '9'): {'shape_id': 'rect_1', 'color': 'blue', 'package_number': 5},
            (no_modifier, 't'): {'tags': 'text_1', 'xy': (100, 30), 'text': 'New Text!', 'package_number': 6},
            (no_modifier, 'c'): {'shape_id': 'text_1', 'color': 'red', 'package_number': 7},
            (no_modifier, 'f'): {'shape_id': 'text_1', 'font_size': 15, 'package_number': 8},
            (modifier_command, 'Left'): {
                'shape_id': 'text_1',
                'delta_x': -10,
                'delta_y': 0,
                'package_number': 9
            },
            (modifier_command, 'Right'): {
                'shape_id': 'text_1',
                'delta_x': 10,
                'delta_y': 0,
                'package_number': 9
            },
            (modifier_command, 'Up'): {
                'shape_id': 'text_1',
                'delta_x': 0,
                'delta_y': -10,
                'package_number': 9
            },
            (modifier_command, 'Down'): {
                'shape_id': 'text_1',
                'delta_x': 0,
                'delta_y': 10,
                'package_number': 9
            },
            (no_modifier, 'BackSpace'): {'shape_id': 'text_1', 'package_number': 10},
            (no_modifier, 'l'): {'xy1': (10, 10),
                                 'xy2': (50, 50),
                                 'width': 3,
                                 'color': 'red',
                                 'arrow_at_end': True,
                                 'tags': ('line_1',),
                                 'package_number': 11
                                 },
            (no_modifier, ';'): {'shape_id': 'line_1', 'coordinates_from': (20, 30), 'coordinates_to': (100, 100),
                                 'package_number': 12},
            (modifier_command, 'BackSpace'): {'shape_id': 'line_1', 'package_number': 13},
            (no_modifier, 'q'): {'shape_id': 'line_1', 'width': 5, 'package_number': 14},
            (modifier_command, 'c'): {'shape_id': 'line_1', 'color': 'yellow', 'package_number': 15},
            (modifier_option, 'Left'): {
                'shape_id': 'line_1',
                'arrow': 'start',
                'package_number': 16
            },
            (modifier_option, 'Right'): {
                'shape_id': 'line_1',
                'arrow': 'end',
                'package_number': 16
            },
            (modifier_option, 'Up'): {
                'shape_id': 'line_1',
                'arrow': 'both',
                'package_number': 16
            },
            (modifier_option, 'Down'): {
                'shape_id': 'line_1',
                'arrow': None,
                'package_number': 16
            },
            (no_modifier, 'z'): {'coordinates_from': (100, 100),
                                 'coordinates_to': (250, 250),
                                 'shape_id': 'rect_1',
                                 'package_number': 17
                                 },
        }

        package_names = ['use_cases.AddRectangle', 'use_cases.RemoveRectangle', 'use_cases.MoveRectangle',
                         'use_cases.SetBorderColor',
                         'use_cases.SetBorderWidth', 'use_cases.SetFillColor', 'use_cases.AddText',
                         'use_cases.SetTextColor',
                         'use_cases.SetTextFontSize', 'use_cases.SetLineWidth', 'use_cases.SetLineColor',
                         'use_cases.SetLineArrow',
                         'use_cases.ChangeRectangleShape']
        command_factories = []
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
            command_factories.append(controller_command)

        # Controller setting
        # Keyboard setting
        def keyboard_shortcut_handler(modifiers: int, key: str):
            request_model = keyboard_shortcut_map.get((modifiers, key), None)
            if request_model is not None:
                n = request_model.get('package_number')
                command_factory = command_factories[n]
                presenter_ = presenters[n]
                command = command_factory(presenter_, request_model)
                command.execute()

        app.set_keyboard_shortcut_handler('root', keyboard_shortcut_handler)

        # Mouse setting
        from mouse import MouseController
        mouse = MouseController()

        def upon_mouse_action(request, ):
            command_factory = request['command_factory']
            presenter_ = request.get('presenter', None)
            if command_factory is not None and presenter_ is not None:
                del request['presenter']
                request.update({'coordinates_from': (10, 10), 'coordinates_to': (request['x'], request['y'])})
                command = command_factory(presenter_, request)
                command.execute()

        mouse.configure(0, upon_mouse_action, mouse.is_left_click, {'shape_id': (f'rect_{1}',),
                                                                    'command_factory': None,
                                                                    })
        mouse.configure(1, upon_mouse_action, mouse.is_left_drag, {'shape_id': (f'rect_{1}',),
                                                                   'command_factory': command_factories[2],
                                                                   'presenter': presenters[2],
                                                                   })
        mouse.configure(2, upon_mouse_action, mouse.is_right_click, {'shape_id': (f'text_{1}',),
                                                                     'command_factory': None,
                                                                     })
        mouse.configure(3, upon_mouse_action, mouse.is_right_drag, {'shape_id': (f'text_{1}',),
                                                                    'command_factory': command_factories[9],
                                                                    'presenter': presenters[9],
                                                                    })
        mouse.configure(4, upon_mouse_action, mouse.is_shift_left_click, {'shape_id': (f'line_{1}',),
                                                                          'command_factory': None,
                                                                          })
        mouse.configure(5, upon_mouse_action, mouse.is_shift_left_drag, {'shape_id': (f'line_{1}',),
                                                                         'command_factory': command_factories[12],
                                                                         'presenter': presenters[12],
                                                                         })
        app.bind_command_to_widget('canvas1', mouse.handle)

        app.launch_app()

    def test_app_encapsulation(self):
        from app import App
        from app_tkinter import app_tkinter_factory
        from complex_commands import instructions as i
        from use_cases import package_names

        app = App(app_tkinter_factory, package_names)

        # Add TextBox
        instruction_green_tb = i.get_instructions_add_text_box('tag1', 'Green Text', 'light green', (10, 10), (100, 20))
        instruction_orange_tb = i.get_instructions_add_text_box('tag2', 'Orange Text', 'orange', (10, 50), (100, 20))
        # ...by shortcut
        app.add_keyboard_shortcut(0, '1', *instruction_green_tb, )
        app.add_keyboard_shortcut(0, '2', *instruction_orange_tb, )

        # ...programmatically
        command_add_green_text_box = app.create_commands(*instruction_green_tb)
        app.execute(command_add_green_text_box)

        # Move TextBox
        instruction_move_left = i.get_instruction_move_left('all', 10)
        instruction_move_right = i.get_instruction_move_right('all', 10)
        instruction_move_up = i.get_instruction_move_up('all', 10)
        instruction_move_down = i.get_instruction_move_down('all', 10)
        app.add_keyboard_shortcut(0, 'Left', *instruction_move_left, )
        app.add_keyboard_shortcut(0, 'Right', *instruction_move_right)
        app.add_keyboard_shortcut(0, 'Up', *instruction_move_up)
        app.add_keyboard_shortcut(0, 'Down', *instruction_move_down)

        # Mouse
        from mouse import MouseController
        mouse = MouseController()
        app._app.bind_command_to_widget('canvas1', mouse.handle)

        # Move Shapes
        mouse.configure(0, app.execute_mouse, mouse.is_left_click, {})
        mouse.configure(1, app.execute_mouse, mouse.is_left_drag, {'instructions': instruction_move_right})

        # Draw Line
        instruction_add_line = (11,), ({'xy1': (10, 10),
                                        'xy2': (100, 100),
                                        'width': 3,
                                        'color': 'green',
                                        'arrow_at_end': True,
                                        'tags': ('line_0',),
                                        'arrow': 'end',
                                        },)
        instruction_move_line = (12,), ({'shape_id': 'line_0', 'coordinates_from': None, 'coordinates_to': None},)
        mouse.configure(2, app.execute_mouse, mouse.is_shift_left_click, {'instructions': instruction_add_line,
                                                                          'save click coordinate': True,
                                                                          'CLICKED_XY': 'xy1',
                                                                          'XY': 'xy2',
                                                                          })
        mouse.configure(3, app.execute_mouse, mouse.is_shift_left_drag, {'instructions': instruction_move_line,
                                                                         'CLICKED_XY': 'coordinates_from',
                                                                         'XY': 'coordinates_to',
                                                                         })

        app.launch_app()


if __name__ == '__main__':
    unittest.main()
