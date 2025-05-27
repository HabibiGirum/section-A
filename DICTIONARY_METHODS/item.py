price = { 'apple': 200, 'orange': 100, 'grapes': 150 }

print(price.items())

prices = {'apple': 200, 'orange': 100, 'grapes': 150}

# using items() to iterate over dictionary
for key, value in prices.items():
    print(f"Key: {key}, Value: {value}")