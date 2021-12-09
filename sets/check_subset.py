def is_subset(a, b):
    if(len(a.difference(b)) == 0):
        print(True)
    else:
        print(False)

A = set('1 2 3 5 6'.split())
B = set('9 8 5 6 3 2 1 4 7'.split())
is_subset(A,B)
A = set('2'.split())
B = set('3 6 5 4 1'.split())
is_subset(A,B)
A = set('1 2 3 5 6 8 9'.split())
B = set('9 8 2'.split())
is_subset(A,B)