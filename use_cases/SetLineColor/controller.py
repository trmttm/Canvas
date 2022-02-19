from .use_case import SetLineColor


def controller_command(presenter, entities):
    command = SetLineColor(presenter, entities)
    return command
