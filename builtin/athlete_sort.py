#!/bin/python3

import math
import os
import random
import re
import sys


num_athletes, num_features = map(int, input().split())
table = [list(map(int, input().split())) for i in range(num_athletes)]
sorting_column = int(input())

sorted_data = sorted(table, key=lambda x: x[sorting_column])

for i in sorted_data:
    print(' '.join(map(str,i)))

