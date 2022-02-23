from .use_case import HighlightTextBox


def controller_command(presenter, entities):
    command = HighlightTextBox(presenter, entities)
    return command
