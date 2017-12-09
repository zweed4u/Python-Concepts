"""
Strategy - need for dynamically changing behavior of class 
abstract strategy class with default set of behaviors
concrete strategy classes with new behaviors

can add methods dynamically by importing types module
"""

import types # support dynamic creation of new types - we're dynamically creating new method types

class Strategy():
	#the stratefy pattern class
	def __init__(self, function=None):
		self.name = "Default Strategy"

		# if a reference to a function is provided, replace the execute() method witht he given function
		if function is not None:
			self.execute = types.MethodType(function, self)

	def execute(self):
		# this gets replaced by another version if another strategy is provided
		# the default method that prints the name of the strategy being used
		print("{} is used!".format(self.name))

# replacement method 1
def strategy_one(self):
	print("{} is used to execute method 1".format(self.name))

# replacement method 2
def strategy_two(self):
	print("{} is used to execute method 2".format(self.name))

# create default strategy
s0 = Strategy()

# execute default strategy
s0.execute()

# create the first variation of our default strategy by providing a new behavior
s1 = Strategy(strategy_one)

# set its name
s1.name = "Strat 1"

# execute the strategy
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strat 2" 
s2.execute()