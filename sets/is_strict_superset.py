# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_strict_superset():
    A = set(input().split())
    n = int(input())
    for i in range(n):
        B = set(input().split())
        if len(B.difference(A)) > 0:
            return False
    return True

print(is_strict_superset())