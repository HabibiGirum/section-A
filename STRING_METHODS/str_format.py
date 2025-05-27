# This code demonstrates how to use the str.format() method in Python to format strings.
# Example 1

phrase = "I like to eat {}s and {}s."

formatted_phrase = phrase.format("apple", "orange")

print(formatted_phrase) # Output: I like to eat apples and oranges.

# Example 2

phrase_1 = "This is {0} and it is a big {1}"

phrase_2 = "This is a big {1} it is {0}"

print(phrase_1.format("AASTU", "University")) # Output: This is AASTU and it is a big University

print(phrase_2.format("AASTU", "University")) # Output: This is a big AASTU it is University
