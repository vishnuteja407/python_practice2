# import re

# def fun(email):
#     pat = r'\b[A-Za-z0-9_+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{1,3}\b'
    
#     if re.match(pat,email):
#         return True
#     else:
#         return False

# def filter_mail(emails):
#     return list(filter(fun, emails))

# if __name__ == '__main__':
#     n = int(input())
#     emails = []
#     for _ in range(n):
#         emails.append(input())

# filtered_emails = filter_mail(emails)
# filtered_emails.sort()
# print(filtered_emails)


import re


email_matcher = re.compile(r'([0-9a-zA-Z_-])+@([a-zA-Z0-9])+\.([a-zA-Z]){1,3}$')

def fun(address):
    return bool(email_matcher.match(address))


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)