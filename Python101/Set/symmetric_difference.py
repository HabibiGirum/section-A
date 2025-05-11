House = {"Cement", "Wood", "Beam", "Rocks"}
Bro_House = {"Clay mud", "Wood", "Beam"}

sym = Bro_House.symmetric_difference(House)
print(f"The materials the me and Bro differ are {sym}")