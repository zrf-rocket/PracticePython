lst = [1, 2, 3, 4, 5]
print(all(x > 0 for x in lst))


tup = (2, 4, 6, 8, 10)
print(all(x % 2 == 0 for x in tup))


s = {'a', 'b', 'c', 'd'}
print(all(x.islower() for x in s))

d = {'a': 1, 'b': 2, 'c': -3, 'd': 4}
print(all(x > 0 for x in d.values()))

lst = []
print(all(lst))

print(all([None]))