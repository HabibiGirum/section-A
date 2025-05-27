data = "50800"

x = data.isdigit() 

print(x) # We expect a True statment from this output. Because all are characters are digits.

# Different examples of isdigit() method

print("12.3".isdigit())      # False
print("½".isdigit())         # False 
print("123a".isdigit())      # False 
print("".isdigit())          # False 

# The isdigit() method can be used to check user input to ensure that it is a number.

user_age = input("Enter your age: ")
if user_age.isdigit():
    age = int(user_age)
    print(f"Your age is {age}.")
else:
    print("Invalid input! Age must be a number.")