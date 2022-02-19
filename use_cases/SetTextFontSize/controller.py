from .use_case import SetTextFontSize


def controller_command(presenter, entities):
    command = SetTextFontSize(presenter, entities)
    return command
