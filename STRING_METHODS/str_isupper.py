data = "THIS IS A TEST!"

x = data.isupper() 

print(x) # Since all the alphabetic characters are uppercase, isupper() will return True.

# Different examples of isupper() method

print("HELLO!123".isupper()) # True (numbers/symbols ignored)
print("".isupper())          # False (empty string)