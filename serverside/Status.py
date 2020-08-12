from enum import Enum


class Status(Enum):
    waiting = 1
    in_game = 2
    game_win = 3
    game_lose = 4
class gameStatus:
    def __init__(self):
        self.current = Status.waiting


    def getStates(self):
        return self.current


    def setIngame(self):
        self.current = Status.in_game
    def setWaiting(self):
        self.current = Status.waiting
    def setWin(self):
        self.current = Status.game_win
    def setLose(self):
        self.current = Status.game_lose