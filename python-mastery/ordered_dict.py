from collections import OrderedDict

ordered_dict = OrderedDict()

n = int(input())
for _ in range(n):
    *item, net_price = input().split()
    item = " ".join(item)
    ordered_dict[item] = ordered_dict.get(item, 0)+ int(net_price)

for item, price in ordered_dict.items():
    print(item, price)