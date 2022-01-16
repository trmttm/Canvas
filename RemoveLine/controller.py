from .use_case import RemoveLine


def controller_command(presenter, kwargs):
    command = RemoveLine(presenter, **kwargs)
    return command
