# age = int(input("What's your age? "))
# age_last_year = age - 1
# print("Last year you were %s." % age_last_year)

# print(type("Hey".replace("ey","i")[-1]))

# firstname = input("Enter first name: ")
# secondname = input("Enter second name: ")
# print("Your first name is %s and your second name is %s" % (firstname, secondname))
import json
from textwrap import indent
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                    {"firstName": "Anna", "lastName": "Smith"},
                    {"firstName": "Peter", "lastName": "Jones"}],
    "owners":[{"firstName": "Jack", "lastName": "Petter"},
              {"firstName": "Jessy", "lastName": "Petter"}]}

# print(d['employees'][1]['lastName'])

# d['employees'][1]['lastName'] = 'smooth'
# d['employees'].append({'firstName': 'Albert', 'lastName': 'Bert'})
# print(d)
with open('company1.json', "w") as f_write:
    json.dump(d, f_write, indent=4)
    # f_write.write(json.dumps(d, indent=2))


with open("company1.json", 'r') as f_read:
    data = json.load(f_read)

# print(data)

with open('company1.json', 'r+') as f_modify:
    data = json.load(f_modify)
    data['employees'].append({'firstName': 'Albert', 'lastName': 'Bert'})
    f_modify.seek(0)
    f_modify.write(json.dumps(data, indent=4))



print(data)







