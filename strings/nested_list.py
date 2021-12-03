scores = [['Harry', 37.21], ['Berry', 37.21],['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
scores2 = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['vikas', 21]]



def find_second_lowest(lst):
    # sort them
    lst.sort(key=lambda x: x[1])
    # grab second lowest:
    second_lowest = list(filter(lambda x: x[1] != lst[0][1], lst))[0][1]
    lst = list(map(lambda x: x[0], filter(lambda x: x[1] == second_lowest, lst)))
    lst.sort()
    return lst

for val in find_second_lowest(scores2):
    print(val)