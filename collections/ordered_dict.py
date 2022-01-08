# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

num_items = int(input())
ord_dict = OrderedDict()
for i in range(num_items):
    inpt = input().split()
    price = int(inpt[-1])
    item_name = ' '.join(inpt[:-1])
    ord_dict[item_name] = ord_dict.setdefault(item_name, 0) + price

for prop in ord_dict.keys():
    print(prop, ord_dict[prop])