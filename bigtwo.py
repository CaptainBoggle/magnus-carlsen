from dictionary import *
import itertools

def rankvalue(card): return dict[card[0]] / 10
def cardvalue(card): return dict[card[0]] + dict[card[-1]]
def seperatehand(hand, suit): return [card for card in hand if card[1] == suit]

def sortcards(cardlist, rank: bool=False):
    """Sorts card using either `rankvalue()` or `cardvalue()`.
    
    If `rank` is true, returns rank. Else, returns total card value."""
    if rank: return [rankvalue(cardrank) for cardrank in cardlist]
    else: return sorted(cardlist, key=cardvalue)

# Single-card section. 
def ishigher(card1, card2):
    """Checks whether `card1` is higher than `card2`."""
    if dict[card1[0]] < dict[card2[0]]: return False
    elif dict[card1[0]] == dict[card2[0]]:
        if dict[card1[1]] <= dict[card2[1]]: return False

    return True

def countcards(hand, roundhistory):
    """Returns cards that have not been played."""
    opponentcards = [cards for cards in allcards if str(roundhistory).count(cards)]
    return set(allcards).difference(hand, opponentcards)

# Two-card section.
def ispair(card1, card2):
    """Checks if two cards are a pair."""
    if card1[0] == card2[0]: return True
    return False

def ispairhigher(pair1, pair2):
    """Checks whether `pair1` is higher than `pair2`."""
    if dict[pair1[0][0]] > dict[pair2[0][0]]: return True
    if dict[pair1[0][0]] == dict[pair2[0][0]]:
        if dict[pair1[0][1]] > dict[pair1[1][1]]: firstsuit = dict[pair1[0][1]]
        else: firstsuit = dict[pair1[1][1]]
        if dict[pair2[0][1]] > dict[pair2[1][1]]: secondsuit = dict[pair2[0][1]]
        else: secondsuit = dict[pair2[1][1]]
        if firstsuit > secondsuit: return True

    return False

def countpairs(hand):
    """Returns legal pairs from `cardlist`."""
    legalpairs = [list(card) for card in list(itertools.combinations(hand, 2)) if ispair(card[0], card[1])]
    return legalpairs

# Three-card section.
def istriple(card1, card2, card3):
    """Checks whether `card1`, `card2` and `card3` are valid triples."""
    if card1[0] == card2[0] == card3[0]: return True
    return False

def istriplehigher(triple1, triple2):
    """Compares triples and checks whether `triple1` is higher than `triple2`."""
    if dict[triple1[0][0]] > dict[triple2[0][0]]: return True
    return False

def counttriples(hand):
    """Returns legal triples from `hand`."""
    return [list(card) for card in list(itertools.combinations(hand, 3)) if istriple(card[0], card[1], card[2])]

# Five-card section.
def isstraight(cards):
    """Checks whether `cards` is a valid straight."""
    sortedhand = sortcards(cards, True)
    if sortedhand == list(range(min(sortedhand), max(sortedhand) + 1)): return True
    return False

def isstraighthigher(stg1, stg2):
    """Compares straights and checks whether `stg1` is higher than `stg2`."""
    stg1 = sortcards(stg1)
    stg2 = sortcards(stg2)

    if dict[stg1[4][0]] > dict[stg2[4][0]]: return True
    elif dict[stg1[4][0]] == dict[stg2[4][0]]:
        if dict[stg1[4][1]] > dict[stg2[4][1]]: return True
        
    return False

def isflush(cards):
    """Checks whether `cards` is a valid flush."""
    cardsets = set()
    for card in sortcards(cards): cardsets.add(card[1])
    if len(cardsets) == 1: return True

    return False

def isflushhigher(flush1, flush2):
    """Checks whether `flush1` is higher than `flush2`."""
    flush1 = sortcards(flush1)
    flush2 = sortcards(flush2)
    
    if dict[flush1[4][1]] > dict[flush2[4][1]]: return True
    elif dict[flush1[4][1]] == dict[flush2[4][1]]:
        if dict[flush1[4][0]] > dict[flush2[4][0]]: return True

    return False

def isfullhouse(cards):
    # Add full house functionality.
    pass

def everyfivecard(hand, type: str=None):
    """Returns every 5-card combination depending on `type`."""
    fivecards = list(itertools.combinations(hand, 5))
    if type == None: return [list(plays) for plays in fivecards]
    if type == "flush": return [list(plays) for plays in fivecards if isflush(plays)]
    if type == "straight": return [list(plays) for plays in fivecards if isstraight(plays)]

# print(everyfivecard(["2S", "3S", "4S", "5S", "6S"], "flush"))

def findlegal(hand, playToBeat, playType: int=1):
    """Finds legal moves with your hand and the current play to beat."""    
    if playType == 1: return sortcards([immigrant for immigrant in hand if ishigher(immigrant, playToBeat[0])])
    if playType == 2: return [pairs for pairs in countpairs(hand) if ispairhigher(pairs, playToBeat)]
    if playType == 3: return [triples for triples in counttriples(hand) if istriplehigher(triples, playToBeat)]
    if playType == 5: pass # 5-card plays

"""
def fullhouse(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    if len(allftypes) != 2:
        return False
    for f in allftypes:
        if allfaces.count(f) == 3:
            allftypes.remove(f)
            return 'full-house', [f, allftypes.pop()]
    else:
        return False

def givefullhousepls(hand):
    for play in everyfivecard:
        set = set()
        for card in play:
            set.add(card[0])
            if len(set) = 2:

              def isfullhouse(cards): #make this not look like bad
                set1 = set()
                counts = {}
                for card in cards:
                  set1.add(card[0])
                if len(set1) != 2:
                  your_answer = False
                else:
                  for card in cards:
                    counts[card[0]] = counts.get(card[0], 0) + 1
                  if counts[list(set1)[0]] == 2 or counts[list(set1)[1]] == 2:
                    if counts[list(set1)[0]] == 3 or counts[list(set1)[1]] == 3:
                      your_answer = True
                    else:
                      your_answer = False
                  else:
                    your_answer = False
                return your_answer
            
              def betterfullhouse(first, second):
                counts1 = {}
                counts2 = {}
                for card in first:
                  counts1[card[0]] = counts1.get(card[0], 0) + 1
                for card in second:
                  counts2[card[0]] = counts2.get(card[0], 0) + 1
                invertdict1 = {v: k for k, v in counts1.items()}
                invertdict2 = {v: k for k, v in counts2.items()}
                if dict[invertdict1[3]] > dict[invertdict2[3]]:
                  your_answer = True
                else: 
                  your_answer = False
                return your_answer
"""        