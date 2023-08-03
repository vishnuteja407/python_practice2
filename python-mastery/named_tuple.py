from collections import namedtuple
N = int(input())
line = input().split()
Student = namedtuple('Student',line)
sum = sum([int(Student(*(input().split())).MARKS) for i in range(N)])/N
print(f"{sum:.2f}")
# print(sum([int(Student(*tuple(input().split())).MARKS) for x in range(N)])/N)
# sum = sum([int(Student(*(input().split())).MARKS) for i in range(N)])/N
# print(sum)
# for i in range(N):
#     st = Student(*(input().split()))
#     sum += int(st.MARKS)
    
# print(f"{sum/N:.2f}")

# 5
# ID         MARKS      NAME       CLASS     
# 1          97         Raymond    7         
# 2          50         Steven     4         
# 3          91         Adrian     9         
# 4          72         Stewart    5         
# 5          80         Peter      6 