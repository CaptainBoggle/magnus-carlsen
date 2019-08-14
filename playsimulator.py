from dictionary import *
from bigtwo import *
import importlib
import random
import struct
import os

class Player:
    def __init__(self, module, playerno, hand):
        self.module = importlib.import_module(module)
        if not hasattr(self.module, "play"): raise RuntimeError("No play function found.")
        self.playerno = playerno
        self.hand = hand
        self.score = 0

    def play(self): return self.module.play(self.hand, False, [], [], self.playerno, (0, 0, 0, 0), (0, 0, 0, 0), 0)
    def delcard(self, card): self.hand.remove(card)
    def addcard(self, card): self.hand.append(card)

class Game:
    def __init__(self):
        self.roundno = 0
        self.players = []
        self.forbidden = []
        self.playtobeat = []
        self.roundhistory = []
        self.roundstart = True

    def fillplayers(self):
        for i in range(4): self.players.append(Player("main", i, self.setuphands()))

    def setuphands(self):
        hand = []
        while True:
            if len(hand) == 13: break
            card = random.choice(allcards)
            if not card in self.forbidden:
                self.forbidden.append(card)
                hand.append(card)
            else: pass
        return hand

cryptseed = struct.unpack("I", os.urandom(4))[0]
print("Using " + str(cryptseed) + " as seed.")
random.seed(cryptseed)

newgame = Game()
newgame.fillplayers()
print(newgame.players[0].play())