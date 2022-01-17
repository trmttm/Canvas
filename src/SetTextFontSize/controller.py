from .use_case import SetTextFontSize


def controller_command(presenter, kwargs):
    command = SetTextFontSize(presenter, **kwargs)
    return command
