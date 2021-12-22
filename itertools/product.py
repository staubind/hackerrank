from itertools import product

# HackerRank asks you to use input() - here I have changed
# the assumption to be that you receive A, B in proper shape
def cart_prod(A, B):
    cart_prod = product(A,B)
    print(' '.join(map(str, cart_prod)))
        
cart_prod()