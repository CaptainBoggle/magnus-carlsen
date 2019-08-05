from dictionary import dict
from bigtwo import *

def play(hand, roundStart, playToBeat, roundHistory, playerNo, handSize, scores, roundNo):
    # If we are starting, play the lowest card or 3 of diamonds.
    if len(playToBeat) == 0:
        if roundStart: return ["3D"]
        else: return [sortcards(hand)[0]]

    return [findlegal(hand, playToBeat, roundStart)[0]]

# play(['3C', '3S', '4D', '8H', '0D', '0C', 'AC', 'AH', 'AS'], False, [], [[[1, ['3D']], [2, ['4C']], [3, []], [0, ['8C']], [1, ['9S']], [2, ['0H']], [3, []], [0, ['0S']], [1, ['JD']], [2, ['JH']], [3, []], [0, ['KC']], [1, []], [2, ['2H']], [3, []], [0, ['2S']], [1, []], [2, []], [3, []]], []], 0, [9, 10, 9, 13], [-3, -9, 36, -24], 1)
# play(['5S'], False, [], [[[3, ['3D']], [0, ['3H']], [1, ['4D']], [2, ['4C']], [3, ['4S']], [0, ['6C']], [1, ['6S']], [2, ['7H']], [3, ['8H']], [0, ['9H']], [1, ['0C']], [2, ['0H']], [3, ['JD']], [0, ['QD']], [1, ['QS']], [2, ['KC']], [3, ['AC']], [0, ['AH']], [1, ['2H']], [2, []], [3, ['2S']], [0, []], [1, []], [2, []]], [[3, ['3S']], [0, ['7S']], [1, ['8C']], [2, ['8S']], [3, ['9C']], [0, ['9S']], [1, ['0S']], [2, ['QC']], [3, ['2D']], [0, ['2C']], [1, []], [2, []], [3, []]], [[0, ['8D']], [1, ['JH']], [2, ['KH']], [3, []], [0, ['AD']], [1, []], [2, []], [3, []]], [[0, ['QH']], [1, ['KD']], [2, ['KS']], [3, []], [0, ['AS']], [1, []], [2, []], [3, []]], []], 0, [1, 4, 5, 4], [-10, 0, 10, 0], 3)
"""
The parameters to this function are:
* `hand`: A list of card strings that are the card(s) in your hand.
* `is_start_of_round`: A Boolean that indicates whether or not the `play` function is being asked to make the first play of a round.
* `play_to_beat`: The current best play of the trick. If no such play exists (you are the first play in the trick), this will be an empty list.
* `round_history`: A list of *trick_history* entries.
A *trick_history* entry is a list of *trick_play* entries.
Each *trick_play* entry is a `(player_no, play)` 2-tuple, where `player_no` is an integer between 0 and 3 (inclusive) indicating which player made the play, and `play` is the play that said player made, which will be a list of card strings.
* `player_no`: An integer between 0 and 3 (inclusive) indicating which player number you are in the game.
* `hand_sizes`: A 4-tuple of integers representing the number of cards each player has in their hand, in player number order. 
* `scores`: A 4-tuple of integers representing the score of each player at the start of this round, in player number order.
* `round_no`: An integer between 0 and 9 (inclusive) indicating which round number is currently being played.

This function should return an empty list (`[]`) to indicate a pass (see "Playing a Round"), or a list of card strings, indicating that you want to play these cards to the table as a valid play.
"""