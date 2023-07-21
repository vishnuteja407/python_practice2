import requests
     
headers = {'User-agent': 'customUserAgent'}
r = requests.get("https://pythonhow.com/media/data/universe.txt", headers = headers)
data = r.text
count = 0
for letter in r.text:
   if letter == 'a':
       count += 1
print(count)



headers = {'User-agent': 'customUserAgent'}
r = requests.get("https://pythonhow.com/media/data/universe.txt", headers = headers)
data = r.text
print(data)
count_a = data.count("a")
print(count_a)