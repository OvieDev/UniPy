from enum import Enum


class CmdArgument(Enum):
    INTEGER = 0
    STRING = 1
    FLOAT = 2
    BOOL = 3
    STRING_ARGS = 4
    HOURDATE = 5 # TODO: implement HOURDATE
