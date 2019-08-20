import timeit

def timefunc(function, *parameters):
    firstrec = timeit.default_timer()
    function(*parameters)
    print(function.__name__ + ": " + str((timeit.default_timer() - firstrec) * 1000) + " milliseconds.")