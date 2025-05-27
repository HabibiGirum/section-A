my_dict = {'a': 1, 'b': 2}
default_value = my_dict.setdefault('c', 3)

print(my_dict) # Output: {'a': 1, 'b': 2, 'c': 3}
print(my_dict.setdefault('a')) # Output: 1
print(my_dict.setdefault('d')) # Output: None
print("Default value provided: ", default_value) # Output: Default value provided:  3