# Example 1
a = list()
a = [] # This expression is equal to "a = list()"

# Example 2 – Append
a = [1, 2, 3]
print(a) # [1, 2, 3]
a.append(4)
print(a) # [1, 2, 3, 4]

# Example 3 – Insert
a.insert(3, 5)
print(a) # [1, 2, 3, 5, 4]

# Example 4 - Add Other Types into the List
a.append('안녕')
a.append(True)
print(a) # [1, 2, 3, 5, 4, '안녕', True]

# Example 5 - Bringing the values out from the List
print(a[3]) # 3
print(a[1:3]) # [2, 3]
print(a[:3]) # [1, 2, 3]
print(a[4:]) # [4, '안녕', True]
print(a[1:4]) # [2, 3, 5]
print(a[1:4:2]) # [2, 5]

# Example 6 - Index Error
# print(a[9]) # IndexError: list index out of range
try:
    print(a[9])
except IndexError:
    print('존재하지 않는 인덱스')

# Example 7 - Delete, Remove
print(a) # [1, 2, 3, 5, 4, '안녕', True]
del a[1]
print(a) # [1, 3, 5, 4, '안녕', True]
a.remove(3)
print(a) # [1, 5, 4, '안녕', True]
print(a.pop(3)) # '안녕'
print(a) # [1, 5, 4, True]