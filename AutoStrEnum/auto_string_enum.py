import inspect
from enum import EnumMeta, Enum

# default logger
# import logging
# logging.basicConfig(level=logging.DEBUG)

# single logger
from SingleLog.log import Logger
logging = Logger('AutoStrEnum',
                 # Logger.DEBUG
                 )


class _MetaData:

    def __init__(self, parent: str, data: str):
        self.parent = parent
        self.data = data

        logging.debug(f'init meta data with {parent}, {data}')

    def __str__(self):
        logging.debug(f'into meta data{inspect.stack()[0][3]}')
        return self.data

    def __repr__(self):
        logging.debug(f'into meta data{inspect.stack()[0][3]}')
        return self.data

    def __eq__(self, other):
        logging.debug(f'into meta data{inspect.stack()[0][3]}')
        if not isinstance(other, _MetaData):
            return False
        if self.parent != other.parent:
            return False
        if self.data != other.data:
            return False
        return True

    def __hash__(self):
        logging.debug(f'into meta data{inspect.stack()[0][3]}')
        return hash(f'{self.parent}{self.data}')


class _MagicMeta(EnumMeta):

    def __contains__(self, other):
        logging.debug(f'into magic meta{inspect.stack()[0][3]}')
        if not isinstance(other, _MetaData):
            return False
        if str(self) != other.parent:
            return False
        return other.data in self.__dict__['_member_names_']

    def __instancecheck__(self, instance):
        logging.debug(f'into magic meta{inspect.stack()[0][3]}')
        if not isinstance(instance, _MetaData):
            return False
        return str(self) == instance.parent

    def __str__(self):
        logging.debug(f'into magic meta{inspect.stack()[0][3]}')
        return str(self.__name__)

    def __repr__(self):
        logging.debug(f'into magic meta{inspect.stack()[0][3]}')
        return str(self.__name__)


generated: dict = {}


class AutoStrEnum(Enum, metaclass=_MagicMeta):
    def __get__(self, instance, owner):
        logging.debug(f'into AutoStrEnum{inspect.stack()[0][3]}')
        global generated

        tuple_key = (str(owner), self.name)
        if tuple_key in generated:
            return generated[tuple_key]

        generated[tuple_key] = _MetaData(parent=str(owner), data=self.name)

        return generated[tuple_key]
