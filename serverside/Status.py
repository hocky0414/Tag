from enum import Enum


class Status(Enum):
    waiting = 1
    in_game = 2
    game_over = 3

class gameStatus:
    def __init__(self):
        self.current = Status.waiting


    def getStates(self):
        return self.current


    def setIngame(self):
        self.current = Status.in_game
    def setWaiting(self):
        self.current = Status.waiting