from .use_case import SetLineArrow


def controller_command(presenter, entities):
    command = SetLineArrow(presenter, entities)
    return command
