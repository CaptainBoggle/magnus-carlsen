from importlib import import_module
from dictionary import allcards
from struct import unpack
from os import urandom
from bigtwo import *
import random

def main():
    # Seed initialisation. Useful for repeating games.
    crypto = unpack("I", urandom(4))[0]
    print("Using", crypto, "as seed.")
    random.seed(crypto)

    bigtwo = Game()
    for i in range(4): bigtwo.addplayer(i)
    bigtwo.revolution(bigtwo.startingplayer().id)

class Player:
    def __init__(self, id, hand):
        if not hasattr(import_module("main"), "play"): raise RuntimeError("No play function found.")
        self.module = import_module("main")
        self.hand = hand
        self.score = 0
        self.id = id

    def play(self, roundstart, playtobeat, rndhistory, id, handsize, scores, round):
        return self.module.play(self.hand, roundstart, playtobeat, rndhistory, id, handsize, scores, round)

    def delcards(self, cards): self.hand = [card for card in self.hand if card not in cards]
    def addcards(self, cards): self.hand += cards

class Game:
    def __init__(self):
        self.roundstart = True
        self.roundhistory = []
        self.playtobeat = []
        self.players = []
        self.roundno = 0
        self.passes = 0

    def revolution(self, index):
        localplayer = self.players[index]
        if self.roundstart and self.roundhistory: self.roundstart = False
        if self.passes == 3: raise RuntimeWarning("One revolution has passed.")

        play = localplayer.play(self.roundstart, self.playtobeat, self.roundhistory, 0, 0, 0, self.roundno)
        if not self.checkcards(localplayer, play): raise RuntimeError("Bot tried to play card(s) not in hand!")
        elif self.compareplays(play): self.addhistory(localplayer.id, play)
        localplayer.delcards(play)

        print("Player", str(localplayer.id) + ":", play, sortcards(localplayer.hand))
        self.revolution((index + 1) % len(self.players))

    def compareplays(self, play):
        if len(play) != len(self.playtobeat):
            if len(play) == 0: self.passes += 1
            elif not "3D" in play: raise RuntimeError("Bot exceeded play to beat limit.")
            else: return True
            return False

        if len(play) == 1: return ishigher(play[0], self.playtobeat[0])
        else: return False

    def fetchcards(self):
        cards = random.sample(allcards, k=13)
        for card in cards: allcards.remove(card)
        return cards

    def addhistory(self, id, cards):
        self.roundhistory.append((id, cards))
        self.playtobeat = cards

    def addplayer(self, id): 
        self.players.append(Player(id, self.fetchcards())) 

    def checkcards(self, player, cards):
        for card in cards:
            if card not in player.hand: return False

        return True

    def startingplayer(self):
        for player in self.players:
            if "3D" in player.hand: return player

        return None

if __name__ == "__main__": main()