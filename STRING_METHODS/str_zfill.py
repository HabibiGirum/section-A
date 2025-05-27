first_string = "Helloworld"
second_string = "@HElloworld"
third_string = "dog"

print(first_string) # Output: Helloworld
print(second_string) # Output: @HElloworld

# If the argument is less than/equal to string length, output will be the same string.
# If the argument is greater than string length, it will be padded with zeros on the left.
 
print(first_string.zfill(10)) #
print(second_string.zfill(10)) 

print(first_string.zfill(12)) # Output: 00Helloworld
print(second_string.zfill(12)) # Output: 00@HElloworld
print(third_string.zfill(12)) # Output: 0000000dog