"""
Builder - solution to antipattern telescoping contructor.
Telescoping contructor is an anti pattern - occurs when there is an excessive number of constructors.
Scenario - building cars (tires, engine, etc.)
Builder - partitions the process of building complex object into 4 roles/participants.
Director - in charge of building product with bulder object.
Abstract Builder - Builder class - provides all necessary interfaces needed to build object.
Concrete Builder - inherits from builder class and implements details of interfaces of builder class for specfic product.
Product - object building be built.
*** Does not rely on polymorphism like factories! Uses divide and conquer strategy ***
"""

class Director():
	def __init__(self, builder):
		self._builder = builder

	def construct_car(self):
		self._builder.create_new_car()
		self._builder.add_model()
		self._builder.add_tires()
		self._builder.add_engine()

	def get_car(self):
		return self._builder.car


class Builder():
	"""
	Abstract Builder. - creates car object and keeps as attribute
	"""
	def __init__(self):
		self.car = None

	def create_new_car(self):
		self.car = Car()


class SkyLarkBuilder(Builder):
	"""
	Concrete Builder -> provides parts and tools to work on the parts
	Inherits from abstract builder but provides methods to be used by director
	"""
	def add_model(self):
		self.car.model = "SkyLark"

	def add_tires(self):
		self.car.tires = "Regular Tires"

	def add_engine(self):
		self.car.engine = "2.4L"

class BugattiBuilder(Builder):
	"""
	Concrete Builder -> provides parts and tools to work on the parts
	Inherits from abstract builder but provides methods to be used by director
	"""
	def add_model(self):
		self.car.model = "Bugatti"

	def add_tires(self):
		self.car.tires = "Sports Tires"

	def add_engine(self):
		self.car.engine = "V6"


class Car():
	"""
	Product - object being built
	"""
	def __init__(self):
		self.model = None
		self.tires = None
		self.engine = None

	def __str__(self):
		return "{} {} {}".format(self.model, self.tires, self.engine)

# Allow director to orchestrate process of car building
builder = SkyLarkBuilder()
another_builder = BugattiBuilder()

director = Director(builder)
another_director = Director(another_builder)

director.construct_car()
another_director.construct_car()

car = director.get_car()
another_car = another_director.get_car()

print(car)
print(another_car)