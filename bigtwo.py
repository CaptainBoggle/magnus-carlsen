from dictionary import dict, allcards

def cardvalue(card): return dict[card[0]] + dict[card[-1]]
def sortcards(cardlist): return sorted(cardlist, key=cardvalue)

def ispair(card1, card2):
    if dict[card1[0]] == dict[card2[0]]: return True
    return False

def ishigherexp(*cards):
    if all(isinstance(card, str) for card in cards):
        if dict[cards[0][0]] < dict[cards[1][0]]: return False
        elif dict[cards[0][0]] == dict[cards[1][0]]:
            if dict[cards[0][1]] <= dict[cards[1][1]]: return False
    elif all(isinstance(card, list) for card in cards):
        if dict[cards[0][0][0]] > dict[cards[1][0][0]]: return True
        elif dict[cards[0][0][0]] == dict[cards[1][0][0]]:
            if dict[cards[0][0][1]] == dict[cards[1][0][1]]:
                pass # At this point, we know that the rank is equal.
                     # To-do: actually finish

# testing 123
# print(ishigherexp("8S", "7S"))

def ishigher(card1, card2):
    """Checks whether `card1` is higher than `card2`."""
    if dict[card1[0]] < dict[card2[0]]: return False
    elif dict[card1[0]] == dict[card2[0]]:
        if dict[card1[1]] <= dict[card2[1]]: return False

    return True

def countcards(hand, roundHistory: list=None):
    """Returns cards that have not been played."""
    opponentcards = [cards for cards in allcards if str(roundHistory).count(cards)]
    return set(allcards).difference(hand, opponentcards)

def findlegal(hand: list=None, playToBeat: list=None, isStartOfRound: bool=None, playType: int=None):
    """Finds legal moves with your hand and the current play to beat."""
    if playType == 1: legal = [immigrant for immigrant in hand if ishigher(immigrant, playToBeat[0])]
    if playType == 2: pass # 2-card plays
    if playType == 3: pass # 3-card plays
    if playType == 5: pass # 5-card plays
    
    return sortcards(legal)