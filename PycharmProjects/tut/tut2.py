# importiert komplette Bibliothek
import math

# importiert einzelne Funtionen

from math import sin
from functools import reduce

print(sin(10))


# lambdas

# map blueprint: map(fct_2_apply, list_of_inputs)
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)

# filter
num_list = list(range(-5, 5))
less_than_zero = list(filter(lambda x: x < 0, num_list))
print(less_than_zero)

# reduce (muss import werden)
product = reduce(lambda x, y: x * y, items)
print(product)

n = 5
array = list(range(0, n - 1))

# geht sicher auch besser


def unique(array):
    c = {}
    for i in array:
        if not(i in c):
            c[i] = 1
        else:
            return False
    return True


print(unique(array))
