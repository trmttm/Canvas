from .use_case import MoveText


def controller_command(presenter, kwargs):
    command = MoveText(presenter, **kwargs)
    return command
