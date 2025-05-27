# Example 1

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print(A.issubset(B)) # Output: True

# Example 2

sA = {(1, 2), (3, 4)}
sB = {(1, 2), (3, 4), (5, 6)}
is_subset = sA.issubset(sB)
print(is_subset)