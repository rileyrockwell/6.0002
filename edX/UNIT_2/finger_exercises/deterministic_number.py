import random

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    random.seed(0)

    # return a 'random' (same number as generated with the previous seed) even number 10 <= x <= 20
    return 2 * random.randint(5, 10)

print(deterministicNumber())