from .use_case import SetFillColor


def controller_command(presenter, kwargs):
    command = SetFillColor(presenter, **kwargs)
    return command
