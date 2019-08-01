from dictionary import dict, allcards

def cardvalue(card): return dict[card[0]] + dict[card[-1]]
def sortcards(cardlist): return sorted(cardlist, key=cardvalue)

def ishigher(card1, card2):
    if dict[card1[0]] < dict[card2[0]]: return False
    elif dict[card1[0]] == dict[card2[0]]:
        if dict[card1[1]] <= dict[card2[1]]: return False

    return True

def countcards(hand: list=None, roundHistory: list=None):
    """Attempts to guess remaining cards. Very WIP."""
    history = str(roundHistory)
    opponentcards = [cards for cards in allcards if history.count(cards)]
    return set(allcards).difference(hand, opponentcards)

def findlegal(hand: list=None, playToBeat: list=None, isStartOfRound: bool=None, playType: int=None):
    """Finds legal moves with your hand and the current play to beat."""

    if playType == 1: legal = [immigrant for immigrant in hand if ishigher(immigrant, playToBeat[0])]
    if playType == 2: pass # 2-card plays
    if playType == 3: pass # 3-card plays
    if playType == 5: pass # 5-card plays
    
    return sortcards(legal)

print(countcards([], [[[1, ['3D']], [2, ['4C']], [3, []], [0, ['8C']], [1, ['9S']], [2, ['0H']], [3, []], [0, ['0S']], [1, ['JD']], [2, ['JH']], [3, []], [0, ['KC']], [1, []], [2, ['2H']], [3, []], [0, ['2S']], [1, []], [2, []], [3, []]], []]))