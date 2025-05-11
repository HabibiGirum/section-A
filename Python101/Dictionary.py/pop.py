prices = {"apple": 100, "banana": 30}

banana_gone = prices.pop("banana")
print(banana_gone) # 30
print(prices)  # {'apple': 100}

carrot_come = prices.pop("carrot", 45)
print(carrot_come) # 45
