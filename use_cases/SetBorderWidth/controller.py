from .use_case import SetBorderWidth


def controller_command(presenter, kwargs):
    command = SetBorderWidth(presenter, **kwargs)
    return command
