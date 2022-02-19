from .use_case import MoveText


def controller_command(presenter, entities):
    command = MoveText(presenter, entities)
    return command
