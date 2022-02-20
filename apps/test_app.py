from importlib import import_module

from app_tkinter import app_tkinter_factory


class TestApp:
    def __init__(self, package_name: str, canvas_color='white'):
        self._package_name = package_name
        self._canvas_color = canvas_color

        # Choose View
        self._view = app_tkinter_factory(canvas_color)

        # Choose presenter & view
        presenter_factory = import_module(f'{package_name}.presenter', '.').presenter_factory
        view_factory = import_module(f'{package_name}.view', '.').view_factory

        self._presenter = presenter_factory()
        view_method = view_factory(self._view)
        self._presenter.attach(view_method)

        # Define controller command
        self._use_case = import_module(f'{package_name}.controller', '.').controller_command

    @property
    def view(self):
        return self._view

    @property
    def use_case_command(self):
        return self._use_case

    @property
    def presenter(self):
        return self._presenter
