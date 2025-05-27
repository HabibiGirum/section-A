# Example 1
# This example demonstrates how to update a dictionary with another dictionary.

dict_a = {'x': 1, 'y': 2}
dict_b = {'y': 3, 'z': 4}
dict_a.update(dict_b)

print(dict_a) 

# Example 2
# This example demonstrates how to update a dictionary with keyword arguments.

dict_a = {'a': 1, 'b': 2}
dict_a.update(c=3, d=4)

print(dict_a)

