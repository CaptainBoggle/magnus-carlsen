from dictionary import *
from itertools import *

def rankvalue(card): return int(dict[card[0]] / 10)
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
    legalpairs = [list(card) for card in combinations(hand, 2) if ispair(card[0], card[1])]
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
    return [list(card) for card in combinations(hand, 3) if istriple(card[0], card[1], card[2])]

# Four-card section (arbitrary card sorting)
def countequalfours(cards):
    """Returns equally ranked quads. Used for Four of a Kinds."""
    return [list(card) for card in combinations(cards, 4) if card[0][0] == card[1][0] == card[2][0] == card[3][0]]

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
    """Checks whether `cards` is a valid full house."""
    cardset = {card[0] for card in cards}
    if len(cardset) != 2: return False
    
    triples = [list(triples) for triples in combinations(cards, 3) if istriple(triples[0], triples[1], triples[2])]
    if len(triples) > 1 or len(triples) == 0:
        cards = triples[0]
        return False

    pairs = [list(pairs) for pairs in combinations(cards, 2) if ispair(pairs[0], pairs[1])]
    if pairs: return True
    return False

def isfullhousehigher(first, second):
    """Checks whether `first` is higher than `second`."""
    first = [list(triple) for triple in combinations(first, 3) if istriple(triple[0], triple[1], triple[2])]
    second = [list(triple) for triple in combinations(second, 3) if istriple(triple[0], triple[1], triple[2])]

    if dict[first[0][0][0]] > dict[second[0][0][0]]: return True
    return False

def isfourofakind(cards):
    """Checks whether `cards` is a valid four of a kind."""
    if countequalfours(cards): return True
    return False

def isfourofakindhigher(first, second):
    """Checks whether `first` is higher than `second`."""
    first = countequalfours(first)
    second = countequalfours(second)

    if dict[first[0][0][0]] > dict[second[0][0][0]]: return True
    return False

# def isfourofakindhigher(first, second):
# rip felix, imagine being 1.5x slower

def isstraightflush(cards):
    if isflush(sortcards(cards)) and isstraight(sortcards(cards)): return True
    else: return False

def fetchtype(cards):
    """Returns type of 5-card play, given an input of `cards`."""
    if isstraight(cards): return "straight"
    elif isflush(cards): return "flush"
    elif isfullhouse(cards): return "fullhouse"

def everyfivecard(hand, type: str=None):
    """Returns every 5-card combination depending on `type`."""
    if type == None: return [list(plays) for plays in combinations(hand, 5)]
    if type == "flush": return [list(plays) for plays in combinations(hand, 5) if isflush(plays)]
    if type == "straight": return [list(plays) for plays in combinations(hand, 5) if isstraight(plays)]
    if type == "fullhouse": return [list(plays) for plays in combinations(hand, 5) if isfullhouse(plays)]

def findlegal(hand, playToBeat, playType: int=1):
    """Finds legal moves with your hand and the current play to beat."""    
    if playType == 5:
        plays = []
        beatType = fetchtype(playToBeat)
        if beatType == "straight": plays += [play for play in everyfivecard(hand, beatType) if isstraighthigher(play, playToBeat)]
        if beatType == "flush": plays += [play for play in everyfivecard(hand, beatType) if isstraighthigher(play, playToBeat)]
        if beatType == "fullhouse": plays += [play for play in everyfivecard(hand, beatType) if isfullhousehigher(play, playToBeat)]
        return plays
    
    if playType == 3: return [triples for triples in counttriples(hand) if istriplehigher(triples, playToBeat)]
    if playType == 2: return [pairs for pairs in countpairs(hand) if ispairhigher(pairs, playToBeat)]
    if playType == 1: return sortcards([immigrant for immigrant in hand if ishigher(immigrant, playToBeat[0])])