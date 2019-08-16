from importlib import import_module
from dictionary import allcards
import itertools as it
import random
import struct
import os

def main():
    # Prints out initial seed. Useful for repeating games.
    cryptseed = struct.unpack("I", os.urandom(4))[0]
    print("Using " + str(cryptseed) + " as seed.")
    random.seed(cryptseed)

    game = Bigtwo()
    game.revolution()

class Player:
    def __init__(self, module, id, hand):
        if not hasattr(import_module(module), "play"): raise RuntimeError("No play function found.")
        self.module = import_module(module)
        self.hand = hand
        self.score = 0
        self.id = id

    def play(self, start, ptb, rh, handsize, scores, roundno):
        return self.module.play(self.hand, start, ptb, rh, self.id, handsize, scores, roundno)

    def delcards(self, cards): 
        for card in cards: self.hand.remove(card)

    def addcards(self, cards): 
        for card in cards: self.hand.append(card)

class Bigtwo:
    def __init__(self):
        self.roundno = 0
        self.players = []
        self.playtobeat = []
        self.roundhistory = []
        self.roundstart = True
        for i in range(4): self.players.append(Player("main", i, self.handoutcards()))

    def revolution(self):
        iter = self.players.index(self.startingplayer())
        
        while True:
            localplayer = self.players[iter]
            playedcards = localplayer.play(self.roundstart, self.playtobeat, self.roundhistory, 0, 0, self.roundno)
            if not self.checkcards(localplayer, playedcards): raise RuntimeError("Bot tried to play card not in hand!")
            localplayer.delcards([card for card in playedcards])
            iter = (iter + 1) % len(self.players)
            print(playedcards)

    def handoutcards(self):
        cards = random.sample(allcards, k=13)
        for card in cards: allcards.remove(card)
        return cards

    def startingplayer(self):
        if self.roundstart:
            for players in self.players:
                if "3D" in players.hand:
                    return players

    def checkcards(self, player, cards):
        for card in cards:
            if not card in player.hand: return False
        return True

if __name__ == "__main__":
    main()