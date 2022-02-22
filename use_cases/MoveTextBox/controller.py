from .use_case import MoveTextBox


def controller_command(presenter, entities):
    command = MoveTextBox(presenter, entities)
    return command
