from .use_case import MoveLine


def controller_command(presenter, kwargs):
    command = MoveLine(presenter, **kwargs)
    return command
