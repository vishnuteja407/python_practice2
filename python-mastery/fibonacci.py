cube = lambda x: x ** 3
fib_list = []
def fibonacci(n):
    # first two terms
    n1, n2 = 0, 1
    count = 0
    # check if the number of terms is valid
    if n <= 0:
        return fib_list
    # if there is only one term, return n1
    elif n == 1:
        fib_list.append(n1)
        return fib_list
    # generate fibonacci sequence
    else:
        while count < n:
            fib_list.append(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
        return fib_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))