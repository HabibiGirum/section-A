data = {
  "name": "kiya",
  "id": "ETS0762/15", 
  "email": "kiyafekadu@gmail.com" ,
  "year": 2015 
}

x = data.get("id")
y= data.get("phone", "not found")

print(x) #output: ETS0762/15
print(y) #output: not found
