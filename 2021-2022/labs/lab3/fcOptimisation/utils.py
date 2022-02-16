from random import uniform

def generateNewValue(lim1, lim2):
    return uniform(lim1, lim2)

def binToInt(x):
    val = 0
    # x.reverse()
    for bit in x:
        val = val * 2 + bit
    return val
