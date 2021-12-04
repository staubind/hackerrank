# Enter your code here. Read input from STDIN. Print output to STDOUT

def count_subscribers():
    input()
    english = set(input().split())
    input()
    french = set(input().split())
    return len(english.union(french))

print(count_subscribers())