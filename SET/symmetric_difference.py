set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {4, 5, 1}

result = set1.symmetric_difference(set2).symmetric_difference(set3)
result2 = set1.symmetric_difference(set2)

print(result) #Output: {5}
print(result2) #Output: {1, 4}
