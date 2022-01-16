from .use_case import SetBorderWidth


def controller_command(presenter, kwargs):
    command = SetBorderWidth(presenter, **kwargs)
    command.execute()
