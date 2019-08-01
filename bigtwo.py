from dictionary import dict, allcards

def cardvalue(card): return dict[card[0]] + dict[card[-1]]
def sortcards(cardlist): return sorted(cardlist, key=cardvalue)

def ishigher(card1, card2):
    if dict[card1[0]] < dict[card2[0]]: return False
    elif dict[card1[0]] == dict[card2[0]]:
        if dict[card1[1]] <= dict[card2[1]]: return False

    return True

def countcards(ourDeck: list=None, opponentPlays: list=None):
    """Attempts to guess remaining cards. Very WIP."""
    maybeRemain = list(set(opponentPlays).difference(allcards))
    maybeRemain = list(set(maybeRemain).difference(ourDeck))

def findlegal(hand: list=None, playToBeat: list=None, isStartOfRound: bool=None, playType: int=None):
    """Finds legal moves with your hand and the current play to beat."""

    if playType == 1: legal = [immigrant for immigrant in hand if ishigher(immigrant, playToBeat[0])]
    if playType == 2: pass # 2-card plays
    if playType == 3: pass # 3-card plays
    if playType == 5: pass # 5-card plays
    
    return sortcards(legal)