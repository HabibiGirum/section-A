data = "This is a string"

check_A = data.endswith("g")
check_B = data.endswith("s")
check_C = data.endswith("st", 5, 12)

print("A: ", check_A)
print("B: ", check_B)
print("C: ", check_C)