from enum import Enum


class TaskType(Enum):
    EASY = 1
    NORMAL = 3
    HARD = 5


class SessionType(Enum):
    SES_CHALLENGE = 0
    SES_COMPUTING = 1
    SES_INDEV = 2
