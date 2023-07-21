import string, os

if not os.path.exists('letters'):
    os.makedirs('letters')

for letter in string.ascii_lowercase:
    with open('letters/'+letter+'.txt', 'w') as f_write:
        f_write.write(letter)