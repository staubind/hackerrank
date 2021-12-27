# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

def calculate_price(supply, demand, s):
    total_earned = 0
    supply = Counter(supply)
    for i in range(len(demand)):
        size = demand[i]
        if supply[size]:
            total_earned += prices[i]
            supply[size] -= 1
    return total_earned
    
num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
num_customers = int(input())
desired_sizes = []
prices = []
for i in range(num_customers):
    inpt = input().split()
    desired_sizes.append(int(inpt[0]))
    prices.append(int(inpt[1]))
print(calculate_price(shoe_sizes, desired_sizes, prices))

