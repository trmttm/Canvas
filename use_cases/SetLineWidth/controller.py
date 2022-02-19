from .use_case import SetLineWidth


def controller_command(presenter, entities):
    command = SetLineWidth(presenter, entities)
    return command
