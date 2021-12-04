# Enter your code here. Read input from STDIN. Print output to STDOUT

def symmetric_dif(a, b):
    n = a.intersection(b)
    u = a.union(b)
    uniques = []
    for item in u:
        if item not in n:
            uniques.append(item)
    for val in sorted(uniques):
        print(val)

def parse_input():
    input()
    a = set(map(int,input().split()))
    input()
    b = set(map(int,input().split()))
    return a, b
if __name__ == '__main__':
    a_set, b_set = parse_input()
    symmetric_dif(a_set, b_set)

a = {2,4,5,9}
b = {2,4,11,12}
symmetric_dif(a,b)
# a = {8, -10}
# b = {5,6,7}
# symmetric_dif(a,b)
a = {50}
b = {100, 150}
symmetric_dif(a,b)
a = {9,10,11}
b = {10,11,13}
symmetric_dif(a,b)