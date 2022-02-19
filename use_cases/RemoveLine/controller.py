from .use_case import RemoveLine


def controller_command(presenter, entities):
    command = RemoveLine(presenter, entities)
    return command
