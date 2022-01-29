# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
inpt = input().split()
nums = list(map(lambda x: int(x) > 0, inpt))
pals = list(map(lambda x: x == x[::-1], inpt))
print(any(pals) if all(nums) else False)