"""
Visitor - allows adding new features to an existing class hierarchy without changing it.
Dynamically add new operations to existing classes with minimal changes.
Scenario-
House class
HVAC specialist - visitor type 1
Electrician - visitor type 2

Visitor pattern represetns new operations to be performed on the various elemnts of an existing class hierarchy
Visitors can provide operations on a composite object
"""

class House():
	# the class being visited
	def accept(self, visitor):
		# interface to accept a visitor
		# triggers the visiting operation
		visitor.visit(self)

	def work_on_hvac(self, hvac_specialist):
		# note that we nw have a reference to the hvac specialist object in the house object
		print(self, "worked on by", hvac_specialist)

	def work_on_electricity(self, electrician):
		# note that we now have a reference to the electrician object in the house object
		print(self, "worked on by", electrician)


	def __str__(self):
		# return the class name when the house object is printed
		return self.__class__.__name__


class Visitor():
	# abstract visitor class 
	def __str__(self):
		# return the class name when the visitor object is printed
		return self.__class__.__name__


class HvacSpecialist(Visitor):
	# inherit from visitor parent class - concrete visitor - hvac specialist
	def visit(self, house):
		house.work_on_hvac(self)
		# the visitor now has a reference to the house object


class Electrician(Visitor):
	# inherit from visitor parent class - concrete visitor - electrician
	def visit(self, house):
		house.work_on_electricity(self)
		# the visitor now has a reference to the house object

# create an hvac specialist
hvac = HvacSpecialist()

# create an electrician
electrician = Electrician()

# create a house
house = House()


# let the house accept the hvac specialist and work on the house by invoking visit() method
house.accept(hvac)

# let the house accept the electrician and work on the house by invoking visit() method
house.accept(electrician)



