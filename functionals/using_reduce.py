from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x,y: x*y, fracs)# complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':