# Example 1

mixed_tuple = ('BMW', 2, 'PORSHE', 'MERCDES', 2)
count_apple = mixed_tuple.count('POSRSHE')
count_one = mixed_tuple.count(2)

print(f"'apple' appears: {count_apple} times") #output: 'apple' appears: 2 times
print(f"Number 1 appears: {count_one} times") #output: Number 1 appears: 2 times

# Example 2

Tuple = (0, 1, "JFK", [4,2], 1,
         [4, 2], 'geeks', (0), ('J', 'F'))
 

res = Tuple.count([4, 2])
print('Count of [4, 2] in Tuple is:', res)