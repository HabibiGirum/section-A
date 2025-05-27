# Example 1

A = {20, 30, 50}
B = {10, 30, 50}

print(A.intersection(B)) # Output: {3, 5}

# Example 2

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = {2, 3, 5, 7, 8}

result = set1.intersection(set2, set3)

print(result)
print("set1 intersection set2 : ",
      set1.intersection(set2))