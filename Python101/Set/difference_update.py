House = {"Cement", "Wood", "Beam", "Rocks"}
Bro_House = {"Clay mud", "Wood", "Beam"}
House.difference_update(Bro_House)

print(House)
print(f"Unlike Bro's my house is made from {House}")