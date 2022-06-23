from enum import Enum


class OperationType(Enum):
    ASSIGN = 0
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    ADDEQ = 5
    SUBEQ = 6
    MULEQ = 7
    DIVEQ = 8
    EQUALS = 9
    NOT = 10
    AND = 11
    OR = 12