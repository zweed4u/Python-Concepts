#!/usr/local/bin/python3.6

"""
Anonymous functions/lambda expressions
Common applications: sorting and filtering data
"""

#Write a function to compute 3x+1
def f(x):
	return (3*x) + 1

assert f(2) == 7

# Converting function to lambda expression
g = lambda x: (3*x) + 1 
assert g(2) == 7


# Multi arg lambda expression
full_name = lambda firstName, lastName: f'{firstName.strip().title()} {lastName.strip().title()}'
print(full_name(' zachary ', 'WEEDEN '))

# lambda expression usage with no name declaration
scifi_authors = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthus C. Clarke', 'Frank Herbert', 'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']
print(scifi_authors)

# Create lambda expression to extract last name and sort using it
# Sort array using lambda expression as key - expression focuses on last name and compares each as lowercase for uniform comparison
scifi_authors.sort(key=lambda name: name.split(' ')[-1].lower())
print(scifi_authors)


# 'Function that makes functions'
def build_quadratic_fn(a, b, c):
	"""
	Returns ax^2 + bx + c
	"""
	return lambda x: (a*x**2)+(b*x)+c

fx = build_quadratic_fn(2, 3, -5)
print(fx(0))
print(fx(1))
print(fx(2))

print(build_quadratic_fn(2, 3, -5)(2))