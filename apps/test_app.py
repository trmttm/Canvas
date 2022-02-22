from importlib import import_module
from typing import Callable

from mouse import MouseController

from app_tkinter import app_tkinter_factory
from entities import Entities


class TestApp:
    def __init__(self, package_name: str, canvas_color='white'):
        # Instantiate Entities
        self._entities = entities = Entities()
        # Choose View
        self._view = app_tkinter_factory(canvas_color)

        # Choose presenter & view
        presenter_factory = import_module(f'{package_name}.presenter', '.').presenter_factory
        view_factory = import_module(f'{package_name}.view', '.').view_factory

        self._presenter = presenter_factory()
        view_method = view_factory(self._view)
        self._presenter.attach(view_method)

        # Define controller command
        command_factory = import_module(f'{package_name}.controller', '.').controller_command
        self._use_case = command_factory(self._presenter, entities)

        self._mouse = MouseController()
        self._mouse_key = 0
        self._view.bind_command_to_widget('canvas1', self._mouse.handle)

    @property
    def entities(self) -> Entities:
        return self._entities

    @property
    def view(self):
        return self._view

    @property
    def use_case_command(self):
        return self._use_case

    def set_keyboard_shortcut_handler(self, keyboard_shortcut_handler):
        self._view.set_keyboard_shortcut_handler('root', keyboard_shortcut_handler)

    @property
    def mouse(self):
        return self._mouse

    def configure_mouse(self, command: Callable, condition, command_specific_arguments_dict: dict = None):
        if command_specific_arguments_dict is None:
            command_specific_arguments_dict = {}
        self._mouse.configure(self._mouse_key, command, condition, command_specific_arguments_dict)
        self._mouse_key += 1

    def launch_app(self):
        self._view.launch_app()
