import array

a1 = array.array('i', [11, 22, 33, 44, 55])
a2 = [11, 22, 33, 44, 55]
a3 = list([11, 22, 33, 44, 55])

print(type(a1), type(a2), type(a3))  # <class 'array.array'> <class 'list'> <class 'list'>
print(a1[1], a2[1], a3[1])
