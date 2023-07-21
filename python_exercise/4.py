
def acceleration(data):
    values =list(map(int, data.split(",")))
    v1 = values[0]
    v2 = values[1]
    t1 = values[2]
    t2 = values[3]
    result = (v2 - v1)/(t2 - t1)
    return result

data = input("Enter input values: ")

func = acceleration(data)
print(func)
