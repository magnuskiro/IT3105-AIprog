__author__ = 'kiro'

hand = []
action = [call, bet, fold]

def setHand(carda, cardb):
    hand.__add__(carda)
    hand.__add__(cardb)
    return 0

def getHand():
    return hand;

# hand probabilities should be dynamic and configured in some kind of config file. So vi can load 10 different playing styles easily.
def getAction(prob):
    if prob < 0.2: x =2
    elif prob >=0.7: x=1
    else: x=0
    return action[x]

