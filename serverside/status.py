from enum import Enum


class Status(Enum):
    waiting = 1
    in_game = 2
    game_over = 3


current = Status.waiting


def getStates():
    return current


def setStates(state):
    current = state
    return current
