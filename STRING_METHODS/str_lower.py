# Example 1
# The .lower() method can be used to compare strings:

string1 = "Section B Students"
string2 = "sECTiOn b sTuDeNtS"

if string1 == string2:
  print("These strings are already the same")
elif string1.lower() == string2.lower():
  print("They are the same when you use the .lower() method")
else:
  print("They are NOT the same")

# Output: They are the same when you use .lower()

#Example 2
#The .lower() method can be used to standardize text that might take different forms, such as user input or the response to an API call:

name = input("What is your name?")
# User writes their name...

if name.lower() == "kiya":
  print("Your name is Kiya!")
else:
  print("Your name is not Kiya.")

#This would print Your name is Kiya! whether the user typed in Kiya, kiya, KIYA, or kIyA.

#Example 3
#The .lower() method does not change the string it is used on:

my_string = "FUN!"

if my_string.lower() == "fun!":
  print("Isn't that just " + my_string)

# Output: "Isn't that just FUN!""