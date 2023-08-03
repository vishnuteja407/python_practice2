import numpy as np

n ,m = map(int, input().split())
myarray = np.array([input().split() for i in range(n)], int)

print(np.mean(myarray, axis = 1))
print(np.var(myarray, axis = 0))
print(round(np.std(myarray),11))
