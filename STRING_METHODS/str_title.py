#Example 1

my_string = "hello, world!"

print(my_string.title())
print(my_string) #output: hello, world!

data = "123abc def"

print(data.title()) #Output: 123Abc Def

#Example 2
#The .title() method can be used to standardize text that might take different forms, such as user input or the response to an API call: 

user_input = input("Enter some text: ")  # User enters "hello world"
titled_text = user_input.title()         # Returns "Hello World"
print(titled_text)