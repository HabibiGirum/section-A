prices = {"apple": 100, "banana": 30}

apple = prices.setdefault("apple", 150)
print(apple)   # 100
print(prices)  # The apple will not be modified

carrot = prices.setdefault("carrot", 45)
print(prices) #{'apple': 100, 'banana': 30, 'carrot': 45}