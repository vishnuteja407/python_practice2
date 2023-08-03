import operator

def person_lister(f):
    def inner(people):
        # complete the function
        age = operator.itemgetter(2)
        people.sort(key=lambda x: int(age(x)))
        return [f(person) for person in people]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


# 3
# Mike Thomson 21 M
# Robert Bustle 31 M
# Andria Bustle 3 F