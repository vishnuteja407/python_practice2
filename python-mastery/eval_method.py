N, m = list(map(int, input().split()))
p = input().replace("x",str(N))
print(True if eval(p) == m else False)

# 1 4
# x**3 + x**2 + x + 1


# >>> input()  
# 1+2
# 3
# >>> company = 'HackerRank'
# >>> website = 'www.hackerrank.com'
# >>> input()
# 'The company name: '+company+' and website: '+website
# 'The company name: HackerRank and website: www.hackerrank.com'