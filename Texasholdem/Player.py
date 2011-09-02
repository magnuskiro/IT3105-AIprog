__author__ = 'kiro'

class Player:
    hand = []
    action = ["call", "bet", "fold"]
    playerNumber = -1

    def __init__(self, cash, number, carda, cardb):
        self.setStartCash(cash)
        self.setPlayerNumber(self,number)
        self.setHand(self, carda, cardb)

    def setStartCash(self, amount):
        self.cash = amount

    def setPlayerNumber(self, n):
        self.playerNumber = n

    def getPlayerNumber(self):
        return self.playerNumber

    def bet(self,amount):
        self.cash -= amount

    def addWinnings(self, amount):
        self.cash += amount

    def setHand(self, carda, cardb):
        self.hand.__add__(carda)
        self.hand.__add__(cardb)
        return 0

    def getHand(self):
        return self.hand;

    # hand probabilities should be dynamic and configured in some kind of config file. So vi can load 10 different playing styles easily.
    def getAction(self, prob):
        if prob < 0.2: x =2
        elif prob >=0.7: x=1
        else: x=0
        return self.action[x]

