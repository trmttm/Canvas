from typing import Dict


class Group:
    def __init__(self):
        self._data: Dict[str, list] = {}

    def add(self, group_name: str, content):
        if group_name in self._all_group_names:
            if content not in self.get_contents(group_name):
                self._data[group_name].append(content)
        else:
            self._data[group_name] = [content]

    def set(self, group_name: str, contents):
        self._data[group_name] = list(contents)

    def remove(self, group_name, contents):
        if group_name in self._data:
            current_contents = self._data[group_name]
            self._data[group_name] = [c for c in current_contents if c not in contents]

    @property
    def _all_group_names(self) -> tuple:
        return tuple(self._data.keys())

    def get_contents(self, group_name: str) -> tuple:
        return tuple(self._data.get(group_name, ()))
