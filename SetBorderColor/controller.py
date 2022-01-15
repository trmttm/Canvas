from .use_case import SetBorderColor


def controller_command(presenter, kwargs):
    command = SetBorderColor(presenter, **kwargs)
    command.execute()
