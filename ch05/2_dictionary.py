# Example 1
a = dict()
a = {} # This is same expression with "a = dict()".

# Example 2 - Make a new dictionary
a = {'key1': 'value1', 'key2': 'value2'}
print(a) # {'key1': 'value1', 'key2': 'value2'}
a['key3'] = 'value3'
print(a) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Example 3 - Get a value from the dictionary
print(a['key1']) # 'value1'

# Example 4 - KeyError
# print(a['key4']) # KeyError
try:
    print(a['key4'])
except KeyError:
    print('존재하지 않는 키')
# del a['key4'] # KeyError
if 'key4' in a:
    print('존재하는 키')
else:
    print('존재하지 않는 키')

# Example 5 - for
for k, v in a.items():
    print(k, v) # key1 value1 ...

# Example 5 - Delete
del a['key1']
print(a) # {'key2': 'value2', 'key3': 'value3'}