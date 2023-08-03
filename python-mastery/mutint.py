class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value


a = MutInt(1)
print(a.value)

a.value = 42

print(a.value)

print(a)