from dictionary import allcards
from bigtwo import *
import timeit
import random

def speedtest(function, *parameters):
    """Prints the time taken to perform `function` with `parameters`.\n
       Useful for determining the speed of certain functions."""
    
    firstrec = timeit.default_timer()
    function(*parameters)
    print(function.__name__ + ": " + str((timeit.default_timer() - firstrec) * 1000) + " milliseconds.")

# Example of how to use (should return 0.01ms):
# speedtest(ishigher, allcards[0], allcards[1])