my_string = "I like chocolates from France"

my_list = my_string.split("\n")

print(my_list)

multiline_string = """
Beets
Bears
Battlestar Galactica
"""

menu = "Breakfast|Eggs|Tomatoes|Beans|Waffles"

list_a = multiline_string.split("\n")

list_b = menu.split("|", 3)

print(f"Using escape characters: {list_a}")

print(f"Limited number of list items: {list_b}")

