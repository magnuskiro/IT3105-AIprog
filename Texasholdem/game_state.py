# The game state will keep necessary information about the 
# state of the game, passing this object between classes and methods
from table import Table

class Game_State:

    def __init__(self):
        self.table = Table()
        self.players = []
        self.small_blind = 0
        self.big_blind = 0
        self.state = "preFlop"

    def initGame(self):

    def addPlayer(self, player):
        self.players.append(player)

    def getPlayers(self):
        return self.players

    def getRemaining(self):
        remaining = []
        for player in self.players:
            if player.in_game:
                remaining.append(player)
        return remaining

    def getLenRemaining(self):
        return len(self.getRemaining())

    def setState(self, newState):
        self.state = newState

    def getState(self):
        return self.state

    def getTable(self):
        return self.table

    def setTable(self, newTable):
        self.table = newTable
        