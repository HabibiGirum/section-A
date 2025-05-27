#Example 1
#Use .find() without specifying the start and end index:

data = "I love to watch a movie"

index1 = data.find("love")
index2 = data.find("eat")
index3 = data.find("to")

print(index1)   # Output: 2
print(index2)  # Output: -1
print(index3)     # Output: 7

#Example 2
#Use .find() with only the start index specified:

data = "I love to watch a movie"

index1 = data.find("love", 2)
index2 = data.find("love", 4)
index3 = data.find("ie", 10)

print(index1)   # Output: 2
print(index2)  # Output: -1
print(index3)     # Output: 7