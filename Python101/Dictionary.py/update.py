prices = {"apple": 100, "banana": 30}
updates = {"banana": 35, "carrots": 45}
prices.update(updates)
print(prices) # banana = 35 and carrot will be added

more = [("potato", 65), ("Tomato", 80)]
prices.update(more)
print(prices)