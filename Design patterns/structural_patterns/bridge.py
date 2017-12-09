"""
Bridge - helps untangle unnecessary complex class hierarchy
eg. Two unrelated abstractions: 1 is implementation specific the other. is impleentation independent
Scenario - 
implementation-independent circle abstraction - how to define the properties of a circle and scale it
implementation-dependent circle abstraction - how to draw a circle
Solution - don't try to abstract both classes in a single class hierarchy
abstract factory and adapter patterns are related to the bridge design pattern
Useful when there are many different kinds of classes involved in hierarchy - separate these classes into different hierarchies	
"""

class DrawingAPIOne():
	# implementation specific abstraction - concrete class one
	def draw_circle(self, x, y, radius):
		print("API 1 drawing a circle at ({}, {} with radius {})".format(x, y, radius))

class DrawingAPITwo():
	# implementation specific abstraction - concrete class two
	def draw_circle(self, x, y, radius):
		print("API 2 drawing a circle at ({}, {} with radius {})".format(x, y, radius))

class Cirlce():
	# implementation specific abstratcion - concrete class two

	def __init__(self, x, y, radius, drawing_api):
		# initialize the necessary attributes
		self._x = x
		self._y = y
		self._radius = radius
		self._drawing_api = drawing_api

	def draw(self):
		# implementation specific abstraction taken care of another class: DrawingAPI***
		self._drawing_api.draw_circle(self._x, self._y, self._radius)

	def scale(self, percent):
		# implementation independent
		self._radius *=percent

# build the first circle object using APIOne
c1 = Cirlce(1, 2, 3, DrawingAPIOne())

# draw a circle
c1.draw()

# build the second circle using APITwo
c2 = Cirlce(4, 5, 6, DrawingAPITwo())

# draw a circle
c2.draw()
