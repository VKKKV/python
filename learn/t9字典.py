# 字典 dict {key:value,...} key:value is one element
# key is string|int|float ,not be list
# value can be any type

# define a null dict
myDict = {}
myDict1 = dict()

# define a dict with data
myDict2 = {'name': 'isaac', 'age': 18, 'like': ['study', 'test'],1: 'test'}
print(myDict2)

# dict have not indexes
# access value through key
print(myDict2['name'])

# if key is not found return error
# .get(key) not found returns None
print(myDict2.get('test'))  # default value is None
print(myDict2.get('test', 1))  # default value is 1

# key int 1 and float 1 are same
# del .pop .clear
del myDict2[1]
print(myDict2)

# .keys .values .items==tuple
for i,j in myDict2.items():
    print(i,j)



# delete the object
del myDict2




