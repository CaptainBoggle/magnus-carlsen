from dictionary import *
from itertools import *

def rankvalue(card): return dict[card[0]] / 10
def cardvalue(card): return dict[card[0]] + dict[card[-1]]
def seperatehand(hand, suit): return [card for card in hand if card[1] == suit]

def sortcards(cardlist, rank: bool=False):
    """Sorts card using either `rankvalue()` or `cardvalue()`.
    
    If `rank` is true, returns rank. Else, returns total card value."""
    if rank: return [rankvalue(cardrank) for cardrank in cardlist]
    else: return sorted(cardlist, key=cardvalue)

# Single-card section. 
def ishigher(first, second):
    """Checks whether `first` is higher than `second`."""
    if dict[first[0]] > dict[second[0]]: return True
    elif dict[first[0]] == dict[second[0]]:
        if dict[first[1]] >= dict[second[1]]: return True

    return False

def countcards(hand, roundhistory):
    """Returns cards that have not been played."""
    opponentcards = [cards for cards in allcards if str(roundhistory).count(cards)]
    return set(allcards).difference(hand, opponentcards)

# Two-card section.
def ispair(first, second):
    """Checks if two cards are a pair."""
    if first[0] == second[0]: return True
    return False

def ispairhigher(first, second):
    """Checks whether `first` is higher than `second`."""
    if dict[first[0][0]] > dict[second[0][0]]: return True
    if dict[first[0][0]] == dict[second[0][0]]:
        if dict[first[0][1]] > dict[first[1][1]]: firstsuit = dict[first[0][1]]
        else: firstsuit = dict[first[1][1]]
        if dict[second[0][1]] > dict[second[1][1]]: secondsuit = dict[second[0][1]]
        else: secondsuit = dict[second[1][1]]
        if firstsuit > secondsuit: return True

    return False

def countpairs(hand):
    """Returns legal pairs from `cardlist`."""
    legalpairs = [list(card) for card in list(combinations(hand, 2)) if ispair(card[0], card[1])]
    return legalpairs

# Three-card section.
def istriple(first, second, third):
    """Checks whether `first`, `second` and `third` are valid triples."""
    if first[0] == second[0] == third[0]: return True
    return False

def istriplehigher(first, second):
    """Compares triples and checks whether `first` is higher than `second`."""
    if dict[first[0][0]] > dict[second[0][0]]: return True
    return False

def counttriples(hand):
    """Returns legal triples from `hand`."""
    return [list(card) for card in list(combinations(hand, 3)) if istriple(card[0], card[1], card[2])]

# Five-card section.
def isstraight(cards):
    """Checks whether `cards` is a valid straight."""
    sortedhand = sortcards(cards, True)
    if sortedhand == list(range(min(sortedhand), max(sortedhand) + 1)): return True
    return False

def isstraighthigher(first, second):
    """Compares straights and checks whether `first` is higher than `second`."""
    first = sortcards(first)
    second = sortcards(second)

    if dict[first[4][0]] > dict[second[4][0]]: return True
    elif dict[first[4][0]] == dict[second[4][0]]:
        if dict[first[4][1]] > dict[second[4][1]]: return True
        
    return False

def isflush(cards):
    """Checks whether `cards` is a valid flush."""
    cardsets = {card[1] for card in cards}
    if len(cardsets) == 1: return True
    return False

def isflushhigher(first, second):
    """Checks whether `first` is higher than `second`."""
    first = sortcards(first)
    second = sortcards(second)
    
    if dict[first[4][1]] > dict[second[4][1]]: return True
    elif dict[first[4][1]] == dict[second[4][1]]:
        if dict[first[4][0]] > dict[second[4][0]]: return True

    return False

def isfullhouse(cards):
    cardset = {card[0] for card in cards}
    if len(cardset) != 2: return False
    
    triples = [list(triples) for triples in combinations(cards, 3) if istriple(triples[0], triples[1], triples[2])]
    if len(triples) > 1 or len(triples) == 0:
        cards = triples[0]
        return False
    
    pairs = [list(pairs) for pairs in combinations(cards, 2) if ispair(pairs[0], pairs[1])]
    if pairs: return True
    return False

def everyfivecard(hand, type: str=None):
    """Returns every 5-card combination depending on `type`."""
    fivecards = list(combinations(hand, 5))
    if type == None: return [list(plays) for plays in fivecards]
    if type == "flush": return [list(plays) for plays in fivecards if isflush(plays)]
    if type == "straight": return [list(plays) for plays in fivecards if isstraight(plays)]

def findlegal(hand, playToBeat, playType: int=1):
    """Finds legal moves with your hand and the current play to beat."""    
    if playType == 1: return sortcards([immigrant for immigrant in hand if ishigher(immigrant, playToBeat[0])])
    if playType == 2: return [pairs for pairs in countpairs(hand) if ispairhigher(pairs, playToBeat)]
    if playType == 3: return [triples for triples in counttriples(hand) if istriplehigher(triples, playToBeat)]
    if playType == 5: pass # 5-card plays    

"""
def isfullhousehigher(first, second):
    counts1 = {}
    counts2 = {}
    for card in first: counts1[card[0]] = counts1.get(card[0], 0) + 1
    for card in second: counts2[card[0]] = counts2.get(card[0], 0) + 1
    invertdict1 = {v: k for k, v in counts1.items()}
    invertdict2 = {v: k for k, v in counts2.items()}
    if dict[invertdict1[3]] > dict[invertdict2[3]]: return True
    return False
"""