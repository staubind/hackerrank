# Enter your code here. Read input from STDIN. Print output to STDOUT

# lower > upper > odds > evens

lower = []
upper = []
odds = []
evens = []

string = input()

for char in string:
    if char.isalpha():
        if char.islower():
            lower.append(char)
        else:
            upper.append(char)
    else:
        if int(char) % 2 == 0:
            evens.append(char)
        else: 
            odds.append(char)
lower.sort()
upper.sort()
odds.sort()
evens.sort()
print(''.join(lower+upper+odds+evens))