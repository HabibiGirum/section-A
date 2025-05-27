data = "This is a test"

x = data.islower()

print(x) # We expect a 'False' value from this statement. Becauese not all the letters are in lowercase.

# Different examples of islower() method

print("hello!123".islower()) # True (numbers/symbols ignored)
print("".islower())          # False (empty string)