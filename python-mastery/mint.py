# mutint.py

from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        return format(self.value, fmt)

    # Implement the "+" operator. Forward operands (MutInt + other)
    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    # Support for reversed operands (other + MutInt)
    __radd__ = __add__

    # Support for in-place update (MutInt += other)
    # Used for assigning a = b and if value of a changes then value of b also change
    def __iadd__(self, other):
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    # Support for equality testing
    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    # One relation is needed for @total_ordering decorator. It fills in others
    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    # Conversions to int() and float()
    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    # Support for indexing s[MutInt]
    __index__ = __int__

a = MutInt(3)
b = MutInt(3)

print(a==b)
print(int(a))

c = MutInt(4)

print(a<c)
print(a<=c)

# b = a

# a += 10

# print(a)

# print(b)

# print(a)

# b = a + 10

# print(b)

# b.value = 23

# print(f'The value is {a:*^10d}')

# a.value = 42

# print(a)

# print(b.value)

# c = a + b
# print(c)

# print(10 + a)

names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']

a = MutInt(1)
print(names[a])