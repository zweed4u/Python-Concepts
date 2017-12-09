"""
Reduce function
"""
import functools # python3 doesn't have builtin reduce() function

# Multiply all numbers in a list
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
muliplier = lambda x,y: x*y
print(functools.reduce(muliplier, data))

# Without reduce function
product = 1
for x in data:
	product = product*x
print(product)