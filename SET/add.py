# Example 1

a = set()
a.add('s')

print(a) #output: {'s'}

a.add('e')

print(a) #output: {'s', 'e'}

a.add('s')

print(a) #output: {'s', 'e'}

# Example 2

prime_numbers = {2, 3, 5, 7}

prime_numbers.add(11)

print(prime_numbers) #output: {2, 3, 5, 7, 11}
