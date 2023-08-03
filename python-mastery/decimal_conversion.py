# def print_formatted(number):
#     for i in range(1, n+1):
#         print(i, oct(i).replace("0o", ''), hex(i).replace("0x","").upper(), bin(i).replace("0b",""), sep='\t')
    

def print_formatted(number):
    width = len(bin(number))-2
    for i in range(1,number+1):
        print(' '.join([rep.rjust(width,' ') for rep in [str(i), oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:]]]))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)