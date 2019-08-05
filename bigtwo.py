from dictionary import dict, allcards
import itertools

def cardvalue(card): return dict[card[0]] + dict[card[-1]]
def sortcards(cardlist): return sorted(cardlist, key=cardvalue)

def countcards(hand, roundhistory):
    """Returns cards that have not been played."""
    opponentcards = [cards for cards in allcards if str(roundhistory).count(cards)]
    return set(allcards).difference(hand, opponentcards)

def ishigher(card1, card2):
    """Checks whether `card1` is higher than `card2`."""
    if dict[card1[0]] < dict[card2[0]]: return False
    elif dict[card1[0]] == dict[card2[0]]:
        if dict[card1[1]] <= dict[card2[1]]: return False

    return True

def ispair(card1, card2):
    """Checks if two cards are a pair."""
    if card1[0] == card2[0]: return True
    return False

def countpairs(hand):
    """Returns legal pairs from `cardlist`."""
    legalpairs = [list(card) for card in list(itertools.combinations(hand, 2)) if ispair(card[0], card[1])]
    return legalpairs

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

def istriple(card1, card2, card3):
    """Checks whether cards are valid triples."""
    if card1[0] == card2[0] == card3[0]: return True
    return False

def istriplehigher(triple1, triple2):
    """Compares triples and checks whether `triple1` is higher than `triple2`."""
    if dict[triple1[0][0]] > dict[triple2[0][0]]: return True
    return False

def counttriples(hand):
    """Returns legal pairs from `cardlist`."""
    legalpairs = [list(card) for card in list(itertools.combinations(hand, 3)) if istriple(card[0], card[1], card[2])]
    return legalpairs

def findlegal(hand, playToBeat, playType: int=1):
    """Finds legal moves with your hand and the current play to beat."""    
    if playType == 1: return sortcards([immigrant for immigrant in hand if ishigher(immigrant, playToBeat[0])])
    if playType == 2: return [pairs for pairs in countpairs(hand) if ispairhigher(pairs, playToBeat)]
    if playType == 3: return [triples for triples in counttriples(hand) if istriplehigher(triples, playToBeat)]
    if playType == 5: pass # 5-card plays