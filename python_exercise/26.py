import datetime
x = datetime.datetime.now()
print(f'Today is {x.strftime("%A, %B %d, %Y")}')

print(x.strftime("Today is %A, %B %d, %Y"))



def age_calculator(age):
    current_year = datetime.datetime.now().year
    year_born = current_year - age
    return year_born

age = int(input("Please enter your age:: "))

y = age_calculator(age)
print(y)