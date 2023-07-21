from math import pi
h = int(input("Enter liquid level: "))

def liquid_volume(h, r=10):
    result = ((4 * pi * r**3) / 3) - (pi * (h ** 2)*(3*r - h))/3
    return result

func = liquid_volume(h)
print(func)