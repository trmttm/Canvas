from .use_case import SetLineArrow


def controller_command(presenter, kwargs):
    command = SetLineArrow(presenter, **kwargs)
    return command
