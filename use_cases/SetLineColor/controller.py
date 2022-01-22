from .use_case import SetLineColor


def controller_command(presenter, kwargs):
    command = SetLineColor(presenter, **kwargs)
    return command
