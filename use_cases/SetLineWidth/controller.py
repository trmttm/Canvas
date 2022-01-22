from .use_case import SetLineWidth


def controller_command(presenter, kwargs):
    command = SetLineWidth(presenter, **kwargs)
    return command
