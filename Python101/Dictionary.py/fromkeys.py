Scorres = [3.4, 2.9, 3.2, 4, 3.2]
for i in Scorres:
    if i>2.5:
        Results = dict.fromkeys(Scorres, "Pass")

print(Results)