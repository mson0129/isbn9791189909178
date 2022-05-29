# Example 1
a = [1, 2, 3, 4, 5]
b = a
print(b)
print(id([1, 2, 3, 4, 5]), id(a), id(b))
a[2] = 4
print(a)
print(b)
print(id([1, 2, 4, 4, 5]), id(a), id(b))

# Example 2
a = [1, 2, 3]
b = a
b[2] = 5
print(a)

# Example 3 – Is the id equal to another?
# Initializing – Make variables as a status of the absence of value from previous example
a = None
# Body
if a is None:
    pass
a = [1, 2, 3]
print(a == a) # True
print(a == list(a)) # True
print(a is a) # True
print(a is list(a)) # False

import copy
a = [1, 2, 3]
print(a == copy.deepcopy(a)) # True
print(a is copy.deepcopy(a)) # False
