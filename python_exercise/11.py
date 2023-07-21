a = [1, 2, 3]
b = (4, 5, 6)
c = list(zip(a,b))
for ele in c:
    print(sum(ele))

for i, j in zip(a, b):
    print(i + j)