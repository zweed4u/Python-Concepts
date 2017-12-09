"""
Singleton - object oriented way of making class attributes global
Only one object instantiated from class.
Useful - an information cache - shared by multiple objects
Modules acts as singletons - shared by multiple objects 

***Borg design pattern implementation***
"""

class Borg():
	"""Borg class making class attributes global"""
	# Attribute dictionary
	_shared_state = {}

	def __init__(self):
		# Make it (shared state) an attribute dictionary
		self.__dict__ = self._shared_state


class Singleton(Borg):
	"""
	Inherits from Borg class - shared state now accessible in here
	This essentially makes the singleton objects and object oriented global
	variable
	"""
	def __init__(self, **kwargs):
		super().__init__()
		#Update the attribute dictionary by inserting a new key-value pair
		self._shared_state.update(kwargs)

	def __str__(self):
		# returns the attribute dictionry for printing
		return str(self._shared_state)


# create a singleton object and add our first acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")
# print the object
print(x)

# creating "another" singleton object and if it refers to the same attribute dictionary by adding another acronym
can_we_make_another = Singleton(SNMP = "Simple Network Management Protocol")

# print the object - retains previous - single instance
print(can_we_make_another)

