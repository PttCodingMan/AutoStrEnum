from enum import EnumMeta, Enum


class _MetaData:

    def __init__(self, parent: str, data: str):
        self.parent = parent
        self.data = data

    def __str__(self):
        return self.data

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, _MetaData):
            return False
        if self.parent != other.parent:
            return False
        if self.data != other.data:
            return False
        return True

    def __hash__(self):
        return hash(f'{self.parent}{self.data}')


class _MagicMeta(EnumMeta):

    def __contains__(self, other):
        if not isinstance(other, _MetaData):
            return False
        if str(self) != other.parent:
            return False
        return other.data in self.__dict__['_member_names_']

    def __instancecheck__(self, instance):
        return str(self) == instance.parent


generate: dict = {}


class AutoStrEnum(Enum, metaclass=_MagicMeta):

    def __get__(self, instance, owner):
        global generate

        tuple_key = (str(owner), self.name)
        if tuple_key in generate:
            return generate[tuple_key]

        generate[tuple_key] = _MetaData(parent=str(owner), data=self.name)

        return generate[tuple_key]