from itertools import cycle, combinations
from dictionary import *
from bigtwo import *
import importlib
import random
import struct
import os

def main():
    # Prints out initial seed. Useful for repeating games.
    cryptseed = struct.unpack("I", os.urandom(4))[0]
    print("Using " + str(cryptseed) + " as seed.")
    random.seed(cryptseed)

    game = Bigtwo()
    print(game.startingplayer())

class Player:
    def __init__(self, module, id, hand):
        self.module = importlib.import_module(module)
        if not hasattr(self.module, "play"): raise RuntimeError("No play function found.")
        self.hand = hand
        self.score = 0
        self.id = id

    def play(self, start, ptb, rh, handsize, scores, roundno):
        return self.module.play(self.hand, start, ptb, rh, self.id, handsize, scores, roundno)

    def delcard(self, card): self.hand.remove(card)
    def addcard(self, card): self.hand.append(card)

class Bigtwo:
    def __init__(self):
        self.roundno = 0
        self.players = []
        self.playtobeat = []
        self.roundhistory = []
        self.roundstart = True

        for i in range(4): self.players.append(Player("main", i, self.handoutcards()))

    def startrevolution(self):
        starter = self.startingplayer()
        starter.play(self.roundstart, self.playtobeat, self.roundhistory, 0, 0, self.roundno)

    def startingplayer(self):
        if self.roundstart:
            for players in self.players:
                if "3D" in players.hand:
                    return players

    def handoutcards(self):
        cards = random.sample(allcards, k=13)
        for card in cards: allcards.remove(card)
        return cards

if __name__ == "__main__":
    main()