import random

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    # recall: randrange(min, max) returns min <= x < max; i.e. 22 to include 20 (to satisfy the constraints)
    return random.randrange(10, 22, 2)


print(stochasticNumber())