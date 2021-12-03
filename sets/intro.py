def average(array):
    # your code goes here
    uniques = set(array)
    return round(float(sum(uniques))/len(uniques), 3)