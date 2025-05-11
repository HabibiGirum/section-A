House = {"Cement", "Wood", "Beam", "Rocks"}
Bro_House = {"Clay mud", "Wood", "Beam"}

House.symmetric_difference_update(Bro_House)

print(House)
print(f"The materials the me and Bro differ are {House}")