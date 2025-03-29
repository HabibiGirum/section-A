# Using str.find() Method Example
text = "The quick brown fox jumps over the lazy dog"

# Finding the position of the word 'fox'
position = text.find('fox')

# Print the result
if position != -1:
    print(f"'fox' found at position: {position}")
else:
    print("'fox' not found in the text")