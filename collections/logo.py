#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict, Counter

def make_logo(string):
    ordict = OrderedDict()
    # count them all
    for letter in string:
        ordict[letter] = ordict.setdefault(letter, 0) + 1
    top_three = sorted(ordict, key=lambda x: (-ordict[x], x))[:3] 
    for letter in top_three:
        print(' '.join([letter, str(ordict[letter])]))

if __name__ == '__main__':
    s = input()
    make_logo(s)
