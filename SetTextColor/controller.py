from .use_case import SetTextColor


def controller_command(presenter, kwargs):
    command = SetTextColor(presenter, **kwargs)
    return command
