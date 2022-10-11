from enum import Enum


class SocketOperationEnum(Enum):
    LOGIN = '1'
    ADD_MOVIE = '1'
    REMOVE_MOVIE = '2'
    SHOW_LIBRARY = '3'
    EXIT = 'q'
    SHUT_DOWN = 'q'
