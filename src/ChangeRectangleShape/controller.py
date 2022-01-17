from .use_case import ChangeRectangleShape


def controller_command(presenter, kwargs):
    command = ChangeRectangleShape(presenter, **kwargs)
    return command
