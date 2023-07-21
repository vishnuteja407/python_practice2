import re
str1 = '''
!Command: show running-config interface mgmt0
!Time: Fri Sep 10 15:13:49 2021

version 7.0(3)I7(1)

interface mgmt0
  vrf member management
  ip address 10.81.59.17/24

'''
str2 = '''
!Command: show running-config interface loopback0
!Time: Fri Sep 10 15:30:01 2021

version 7.0(3)I7(5) Bios:version 07.64

interface loopback0
  ip address 30.8.0.3/32


'''

result = []
def commandValidator(str1):  
    for data in str1.split("\n"):
        match = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|(vrf member [a-zA-Z0-9]+)', data)
        if match:
            result.append(match.group(0))
            if len(result)>1:
                return (f'{result[1]} {result[0].split(" ")[0]} {result[0].split(" ")[2]}')
            else:
                return (f'{result[0]}')


print(commandValidator(str1))