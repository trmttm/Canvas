from importlib import import_module
from typing import Callable
from typing import Iterable
from typing import List

from interface_view import ViewABC


class App:
    _package_number = 'package_number'
    _instructions = 'instructions'

    def __init__(self, app_factory: Callable[[], ViewABC], package_names: List[str]):
        self._app = app_factory()
        self._command_factories = []
        self._presenters = []
        self._views = []
        for package_number, package_name in enumerate(package_names):
            # Choose presenter & view
            presenter_factory = import_module(f'{package_name}.presenter', '.').presenter_factory
            view_factory = import_module(f'{package_name}.view', '.').view_factory

            self._presenters.append(presenter_factory())
            self._views.append(view_factory(self._app))
            presenter = self._presenters[package_number]
            view = self._views[package_number]
            presenter.attach(view)

            # Define controller command
            controller_command = import_module(f'{package_name}.controller', '.').controller_command
            self._command_factories.append(controller_command)

        self._keyboard_shortcut_map = {}

    def add_keyboard_shortcut(self, modifier, key, package_numbers: Iterable[int], request_models: Iterable[dict]):
        commands = self.create_commands(package_numbers, request_models)
        self._keyboard_shortcut_map[(modifier, key)] = commands

    def create_commands(self, package_numbers, request_models):
        commands = []
        for package_number, request_model in zip(package_numbers, request_models):
            command = self._create_command(package_number, request_model)
            commands.append(command)
        return commands

    def _create_command(self, package_number: int, request_model: dict) -> Callable:
        command_factory = self._command_factories[package_number]
        presenter_ = self._presenters[package_number]
        command = command_factory(presenter_, request_model)
        return command

    @staticmethod
    def execute(commands: Iterable):
        for command in commands:
            command.execute()

    def execute_mouse(self, request):
        package_numbers, request_models = request.get(self._instructions, ((), ()))
        n = max(len(package_numbers), 1)
        # delta will be applied to the same tag n times.
        request['delta_x'] /= n
        request['delta_y'] /= n

        x_option = request.get('X', None)
        y_option = request.get('Y', None)
        xy_option = request.get('XY', None)
        last_x_option = request.get('LAST_X', None)
        last_y_option = request.get('LAST_Y', None)
        last_xy_option = request.get('LAST_XY', None)
        clicked_x_option = request.get('CLICKED_X', None)
        clicked_y_option = request.get('CLICKED_Y', None)
        clicked_xy_option = request.get('CLICKED_XY', None)
        x = request['x']
        y = request['y']
        last_x = x - request['delta_x']
        last_y = y - request['delta_y']
        clicked_x, clicked_y = request['coordinates'][0]

        """
        Directly invokes presenter, as opposed to instantiating UseCases commands.
        This is because request_model cannot be determined until mouse input is provided.
        """
        for package_number, request_model in zip(package_numbers, request_models):
            presenter_ = self._presenters[package_number]
            request_model.update(request)

            """
            Assign current mouse x,y to option dynamically.
            """

            if x_option is not None:
                request_model[x_option] = x
            if y_option is not None:
                request_model[y_option] = y
            if xy_option is not None:
                request_model[xy_option] = x, y
            if last_x_option is not None:
                request_model[last_x_option] = last_x
            if last_y_option is not None:
                request_model[last_y_option] = last_y
            if last_xy_option is not None:
                request_model[last_xy_option] = last_x, last_y
            if clicked_x_option is not None:
                request_model[clicked_x_option] = clicked_x
            if clicked_y_option is not None:
                request_model[clicked_y_option] = clicked_y
            if clicked_xy_option is not None:
                request_model[clicked_xy_option] = clicked_x, clicked_y
            presenter_.present(**request_model)  # Directly invoking presenter

    def _assign_keyboard_shortcuts(self):
        def keyboard_shortcut_handler(modifiers: int, key: str):
            commands = self._keyboard_shortcut_map.get((modifiers, key), ())
            for command in commands:
                command.execute()

        self._app.set_keyboard_shortcut_handler('root', keyboard_shortcut_handler)

    def bind_command_to_widget(self, widget_id, command):
        self._app.bind_command_to_widget(widget_id, command)

    def launch_app(self):
        self._assign_keyboard_shortcuts()
        self._app.launch_app()
