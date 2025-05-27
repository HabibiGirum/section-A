#Example 1

data = "Hello, World!"

new_string = data.swapcase()

print(new_string)

# Output: "hELLO, wORLD!"

#Example 2
#The .swapcase() method does not change the string it is used on

my_string = "camelCasingIsFun"

my_string.swapcase()

print(my_string)
print(my_string.swapcase())