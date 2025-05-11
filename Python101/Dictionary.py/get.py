prices = {"apple": 100, "banana": 30}

print(prices.get("apple"))      # 100
print(prices.get("orange"))     # None
print(prices.get("orange", 0))  # 0 