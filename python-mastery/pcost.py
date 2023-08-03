# total_cost = 0.0

# with open("Data/portfolio.dat", 'r') as data:
#     read_data = data.readlines()
#     for line in read_data:
#         values = line.split()
#         quantity = int(values[1])
#         price = float(values[2])
#         total_cost = total_cost + (quantity * price)
#     print(total_cost)


# pcost.py

# total_cost = 0.0

# with open('Data/portfolio.dat', 'r') as f:
#     for line in f:
#         fields = line.split()
#         nshares = int(fields[1])
#         price = float(fields[2])
#         total_cost = total_cost + nshares * price

# print(total_cost)




def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'r') as f:
        for line in f:
            try:
                fields = line.split()
                nshares = int(fields[1])
                price = float(fields[2])
                total_cost = total_cost + nshares * price
            except Exception as e:
                print("Invalid data", repr(line))
                print("Exception", e.__class__)
                print("Reason:", e)
    return total_cost

if __name__ == '__main__':
    print(portfolio_cost('Data/portfolio.dat'))


#python3 -i pcost.py


