from bigtwo import *
import time

def timefunc(function, *parameters: list):
    firstrec = time.time()
    function(parameters)
    secndrec = time.time()
    return str(secndrec - firstrec)

print(timefunc(isfourofakind, ["2D", "2H", "2C", "2S", "4H"]))
# Broke with more than one argument.