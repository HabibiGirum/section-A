# Example 1

A = {'a', 'b', 'c', 'd'}
B = {'c', 'f', 'g'}

print(A.difference(B))
print(B.difference(A))

# Example 2

A = {10, 20, 30, 40, 50}
B = {30, 40, 50, 60, 70}
C = {50, 60, 70, 80, 90}

result = A.difference(B, C)  
result2 = B.difference(A, C)
result3 = C.difference(A, B)

print(result) #output: {10, 20}
print(result2) #output: set()
print(result3) #output: {80, 90}