"""
Prototype - clones objects according to prototypical instance
useful when creating many identical objects individually
Scenario - building car - mass production
clone instead of creating objects one at a time.
Create prototypical instance at first and then clone it whenever you need replica
Related to abstract factory pattern
"""
import copy

class Prototype():
	def __init__(self):
		"""
		creating dictionary object - contains object to be cloned
		"""
		self._objects = {}

	def register_object(self, name, obj):
		"""
		Registering object to be cloned - name used as key when storing in dict
		{"name_string": object}
		"""
		self._objects[name] = obj

	def unregister_object(self, name):
		"""
		Unregister or delete objects from dictionary object
		"""
		del self._objects[name]

	def clone(self, name, **attr):
		"""
		Clone a registered object and update its attributes
		"""
		obj = copy.deepcopy(self._objects[name])
		obj.__dict__.update(attr)
		return obj


class Car():
	def __init__(self):
		self.name = "Bugatti"
		self.color = "Blue"
		self.options = "Sport"

	def __str__(self):
		return "{} {} {}".format(self.name, self.color, self.options)

# Prototypical object to be cloned
car = Car()

prototype = Prototype()
prototype.register_object("bugatti", car)

car2 = prototype.clone("bugatti")

print(car)
print(car2)

