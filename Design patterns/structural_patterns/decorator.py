"""
Decorator - add addtitional features to an existing object dynamically without subclassing
Scenario - function that displays 'hello world' and then we'd like to make it look fancier with additional text
Adaptor, composite and strategy are all patterns related to decorator pattern
"""

from functools import wraps

def make_blink(function):
	"""
	Defines the decorator
	"""
	# make the decorator transparent in terms of its name and docstring
	@wraps(function)

	# define the innter function
	def decorator():
		# grab the return value of the function being decorated
		ret = function()

		# add new functionality of the funciton being decorated
		return "<blink>{}</blink>".format(ret)

	return decorator

# apply decorator
@make_blink
def hello_world():
	"""
	Original function
	"""
	return "Hello World"

# check the result of decorating
print(hello_world())

# check if the function name is still the name of the function being decorated (name of function not name of decorator)
print(hello_world.__name__)

# check if the docstring is still the same as that of the function being decorated (docstring of function not of docstring)
print(hello_world.__doc__)
