Scorres = [3.4, 2.9, 3.2, 4, 3.2]
highest = Scorres[0]
for i in Scorres:
    if i > highest:
        highest = i

print(highest)
print(f"The highest score is found on index {Scorres.index(highest)}")