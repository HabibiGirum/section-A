data_1 = 'Lèarning Pythön!'
data_2 = 'Consistèntly!'

default_example = data_1.encode()
ascii_example = data_2.encode(encoding='ascii', errors='xmlcharrefreplace')

print("Default example:", default_example)
print("ASCII example:", ascii_example)