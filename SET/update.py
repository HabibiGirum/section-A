# Example 1

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.update(set2)

print(set1)

# Example 2

set1 = {'class', 'lists'}
list1 = [1, 'sets', 2.5]

set1.update(list1)

print(set1)

# Example 3

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {1, 2}

d2.update(d1.keys())

print(d2)