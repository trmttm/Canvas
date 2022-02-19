from .use_case import MoveLine


def controller_command(presenter, entities):
    command = MoveLine(presenter, entities)
    return command
