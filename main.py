from dictionary import dict
from bigtwo import *

# Bot works and can play 2-card plays.
# When start of trick, magnus-carlsen only plays 1 card.
# fix pls

def play(hand, roundStart, playToBeat, roundHistory, playerNo, handSize, scores, roundNo):
    # If we are starting, play the lowest card or 3 of diamonds.
    if len(playToBeat) == 0:
        if roundStart: return ["3D"]
        else: return [sortcards(hand)[0]]
    elif len(playToBeat) == 1: 
        try: return [findlegal(hand, playToBeat, 1)[0]]
        except IndexError: return []
    elif len(playToBeat) == 2: 
        try: return findlegal(hand, playToBeat, 2)[0]
        except IndexError: return []
    elif len(playToBeat) == 3:
        try: return findlegal(hand, playToBeat, 3)[0]
        except IndexError: return []

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

if __name__ == '__main__':
  # Write your own test cases for your `play` function here.
  # These can be run with the Run button and will not affect the tournament or marking.
  
  # Here's an example test case and testing code to kick you off.
  TESTS = [  # [ expected return value, inputs ]
    [['3D'], [['3D', '4D', '4H', '7D', '8D', '8H', '0D', '0C', 'JH', 'QC', 'QS', 'KH', 'AS'], True, [], [[]], 0, [13, 13, 13, 13], [0, 0, 0, 0], 0]],
    # Add more tests here.
  ]
  
  # This runs the above test cases.
  for i, test in enumerate(TESTS):
    expected_return_value, inputs = test
    actual_return_value = play(*inputs)
    if actual_return_value == expected_return_value:
      print('PASSED {}/{}.'.format(i + 1, len(TESTS)))
    else:
      print('FAILED {}/{}.'.format(i + 1, len(TESTS)))
      print('    inputs:', repr(inputs))
      print('  expected:', repr(expected_return_value))
      print('    actual:', repr(actual_return_value))