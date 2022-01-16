from .use_case import AddLine


def controller_command(presenter, kwargs):
    command = AddLine(presenter, **kwargs)
    return command
