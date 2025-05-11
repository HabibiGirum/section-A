# STRING METHODS 
# str.lower() Method
The "str.lower()" method is a built-in Python string method used to convert all characters in a string to lowercase. This method does not take any parameters. The method returns a new string where all uppercase characters in the original string are converted to lowercase.
The method scans each character in the string. If the character is uppercase, it converts it to its lowercase equivalent.Non-alphabetic characters remain unchanged.
N.B. The original string is not modified. Instead, a new string is returned with all characters converted to lowercase.

# str.upper() Method
The str.upper() method converts all lowercase characters in a string to uppercase. Just like str.lower() it does not modify the original string; instead, it returns a new string with all characters in uppercase. Also this method does not take any parameters. 
It returns a new string where all lowercase characters are converted to uppercase. Non-alphabetic characters and the one's which are already an uppercase remain unchanged.
N.B. Like the previous one the original string is not modified. Instead, a new string is returned with all characters converted to uppercase.

# str.capitalize()
The capitalize() method in Python is a string method that returns a copy of the original string with the first character capitalized and the rest of the characters in lowercase. If the string is empty or the first character is already capitalized, the method will return the string as is.

# isupper()
The isupper() method in Python is used to check if all the alphabetic characters in a string are uppercase. If all letters are uppercase, it returns True, otherwise, it returns False. The method only checks alphabetic characters; numbers and symbols do not affect the result.
If the string contains at least one lowercase letter, it returns False.

# islower()
The islower() method in Python is a string method that checks whether all characters (letters) in the string are lowercase. If all the characters are lowercase, it returns True; otherwise, it returns False. Non-alphabetic characters (like numbers, symbols, or whitespace) are ignored and do not affect the result.
like isupper() this method does not take any parameters.

# str.swapcase()
The swapcase() method is a string method that returns a new string where all the uppercase letters are converted to lowercase, and all the lowercase letters are converted to uppercase. Non-alphabetic characters (like numbers, symbols, or whitespace) remain unchanged.
Again this method does not take any parameters.It returns a new string with the case of each character swapped.

# str.title()
The str.title() method in Python is a string method that returns a new string where the first character of each word is capitalized (title case), and the rest of the characters in each word are lowercase. Words are considered to be sequences of characters separated by whitespace.
You might have noticed that this method is used to modify the capitalization of strings like the capitalize method, but they behave differently. While capitilize method capitalizes only the first character of the "string", the title method first character of each "word".

# str.find()
The find() method is a string method that searches for the first occurrence of a substring within the string. If the substring is found, it returns the index of the first character of the substring. If the substring is not found, it returns -1.
SYNTAX: string.find(substring, start, end)
    substring: The substring to search for in the string.
    start (optional): The starting index within the string where the search begins. Default is 0.
    end (optional): The ending index within the string where the search ends. Default is the end of the string.

# str.index()
The index() method in Python is a string method that searches for the first occurrence of a substring within the string. If the substring is found, it returns the index of the first character of the substring. If the substring is not found, it raises a ValueError.
SYNTAX: string.index(substring, start, end)
    substring: The substring to search for in the string.
    start (optional): The starting index within the string where the search begins. Default is 0.
    end (optional): The ending index within the string where the search ends. Default is the end of the string.

# str.count()
The count() method in Python is a string method that returns the number of non-overlapping occurrences of a substring within the string. If the substring is not found, it returns 0.
SYNTAX: string.count(substring, start, end)
    substring: The substring to count occurrences of in the string.
    start (optional): The starting index within the string where the search begins. Default is 0.
    end (optional): The ending index within the string where the search ends. Default is the end of the string.

# str.replace()
The replace() method in Python is a string method that returns a new string where all occurrences of a specified substring are replaced with another substring.
SYNTAX: string.replace(old, new, count)
    old: The substring to be replaced.
    new: The substring to replace the old substring.
    count (optional): The maximum number of occurrences to replace. If not specified, all occurrences are replaced.

# str.startswith()
The startswith() method in Python is a string method that checks whether the string starts with a specified substring. It returns True if the string starts with the substring, otherwise False.
SYNTAX: string.startswith(prefix, start, end)
    prefix: The substring to check at the beginning of the string.
    start (optional): The starting index within the string where the check begins. Default is 0.
    end (optional): The ending index within the string where the check ends. Default is the end of the string.

# str.endswith()
The endswith() method in Python is a string method that checks whether the string ends with a specified substring. It returns True if the string ends with the substring, otherwise False.
SYNTAX: string.endswith(suffix, start, end)
    suffix: The substring to check at the end of the string.
    start (optional): The starting index within the string where the check begins. Default is 0.
    end (optional): The ending index within the string where the check ends. Default is the end of the string.

# str.strip()
The strip() method in Python is a string method that removes leading and trailing whitespace (spaces, tabs, and newlines) from the string. It can also remove specified characters if provided. The resulting valaue will be a new string with leading and trailing characters removed.
SYNTAX: string.strip([chars])
    The parameter chars (optional) is a string specifying the characters to remove. If not provided, it removes whitespace by default.

# str.lstrip()
The lstrip() method in Python is a string method that removes leading whitespace (or specified characters) from the string. It only affects the left side (beginning) of the string. This method results a new string with leading characters removed.
SYNTAX: string.lstrip([chars])
    Again the parameter arameters chars (optional) is a string specifying the characters to remove. If not provided, it removes whitespace by default.

# str.rstrip()
The rstrip() method in Python is a string method that removes trailing whitespace (or specified characters) from the string. It only affects the right side (end) of the string. Tis one will result a new string with trailing characters removed.
SYNTAX: string.lstrip([chars])
    Again the parameter arameters chars (optional) is a string specifying the characters to remove. If not provided, it removes whitespace by default.

# str.split()
This method splits a string into a list of substrings by breaking it at each occurrence of a specified delimiter.
SYNTAX: string.split(sep=None, maxsplit=-1)
    sep: Delimiter (default: whitespace). If not specified, splits on any whitespace.
    maxsplit: Maximum number of splits (default: -1, meaning all occurrences).

# str.join()
This method takes an iterable (list, tuple, etc.) of strings and concatenates them into a single string, with the original string used as the separator. If the iterable contains non-strings (e.g., integers), it raises a TypeError. T fix that we have to convert them to strings first.
SYNTAX: separator.join(iterable)
    iterable: List, tuple, etc., containing strings to join.
    separator: String used to join the elements.

# str.format()
The str.format() method is a string formatting tool in Python that replaces placeholders ({}) in a string with specified values. 
SYNTAX: "Template with {} placeholders".format(values)
    The {} acts as a placeholder
    Values are passed to .format() in order

# str.isalpha()
This method checks if all characters in the string are alphabetic (letters) and if the string is not empty. The method returns True only if all characters are letters and also if the string has at least one character. It will returns False for empty strings and if they are strings with spaces, numbers, or symbols (e.g., "Hello!", "Python3").

# str.isdigital()
This one you might say is the opposite of the  str.isalpha() method, in which this method checks if all characters in the string are digits (0-9) and the string is not empty.The method returns True only if all characters are digits (0-9) and that the string has at least one character.It will returns False for empty strings and strings with spaces, decimals, signs, or letters (e.g., "-123", "3.14", "0xFF").

# str.isalnum()
This one is like merging the above two methods in to one (isalpha + isdigit). This method checks if all characters are alphanumeric (letters or digits) and the string is not empty.The method returns True if all characters are letters (A-Z, a-z) or digits (0-9) and the string has at least one character. It will returns False for empty strings and strings with spaces or symbols (e.g., "Hello!", "code 4").

# str.isspace() Method in Python
The isspace() method checks if all characters in a string are whitespace characters and the string is not empty. Whitespace Characters Include: Space ( ), Tab (\t), Newline (\n), Carriage return (\r), Vertical tab (\v), Form feed (\f)

# f-strings (Formatted String Literals)
f-strings are a way to embed expressions inside string literals. They are the fastest and most readable method for string formatting. They are used writing an f or F before the string, then place expressions inside {} that get evaluated at runtime. This method can be used on all Python expressions, including function calls, arithmetic, etc.

# len() 
This method returns the length (number of items) of an object. It is mostly used in Strings (counts characters), Lists, tuples, sets (counts elements), Dictionaries (counts keys), Bytes, bytearrays, etc.

# str.encode()
This method is used in converting a string to a bytes object (the way computers store data) using a specified encoding (default: UTF-8).
SYNTAX: str.encode(encoding="utf-8", errors="strict")
    encoding: The character encoding to use (common ones: "utf-8", "ascii", "latin-1").
    errors: How to handle encoding problems:
        strict (default): Raise an error
        ignore: Skip problematic characters
        replace: Use a replacement marker (�)
Note: There is another method the is called str.decode which decodes the string that the str.encode() made. You can see it on the py file
We use this methode when saving text to binary files (open(filename, "wb")), when sending data over networks (HTTP, sockets), or when working with libraries that require bytes (like some cryptographic functions).