# # Enter your code here. Read input from STDIN. Print output to STDOUT

# def int_division(a, b):
#     try:
#         print (int(a) / int(b))
#     except ZeroDivisionError as e1:
#         print("Error code:", e1)
#     except ValueError as e2:
#         print("Error code:", e2)
    
# if __name__ == "__main__":
#     n = int(input())
    
#     for _ in range(n):
#         a, b = input("").split()
#     int_division(a, b)


N = int(input())
for i in range(N):
    try:
        a,b =list(map(int,input().split()))
        print("{}".format(int(a//b)))
    except Exception as e:
        print ("Error Code:",e)