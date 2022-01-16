from .use_case import AddRectangle


def controller_command(presenter, kwargs):
    command = AddRectangle(presenter, **kwargs)
    return command
