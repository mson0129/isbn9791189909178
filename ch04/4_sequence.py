# Example 1
a = 'abc'
a = 'def'
print(type(a))

# Example 2
a = 'abc'
print(id('abc'))
print(id(a))
a = 'def'
print(id('def'))
print(id(a))

# Example 3 - There is an error.
a[1] = 'd'