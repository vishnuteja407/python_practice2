inx = (input().strip()).split()
n = int(inx[0])
m = int(inx[1])
dash = '---'
dots = '.|.'

x = int((n-1)/2)
for i in range(n) :
    if i % 2 != 0:
        print(dash*x + dots*i + dash*x)
        x -= 1
        
        
xm = int(((m-7)/2))
print('-'*xm + "WELCOME" + '-'*xm)


z = 1
for i in range(n) :
    if i % 2 != 0:
        print(dash*z + dots*((n-1) - i) + dash*z)
        z += 1