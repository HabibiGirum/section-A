A = {'a', 'c', 'd'}
B = {'c', 'd', 2 }
C = {1, 2, 3}

print('A U B =', A.union(B)) # Output: {'a', 2, 'c', 'd'}
print('A U C =', A.union(C)) # Output: {'a', 1, 2, 'c', 'd'}
print('B U C =', B.union(C)) # Output: {1, 2, 'c', 'd'}
print('A U B U C =', A.union(B, C)) # Output: {1, 2, 'a', 'c', 'd'}
print('A.union() =', A.union()) # Output: {'a', 'c', 'd'}