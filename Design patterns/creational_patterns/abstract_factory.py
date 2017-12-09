"""
Abstract Factory Pattern example - creational design pattern
Scenario: Pet factory - concrete factory includes dog and cat factory - 
produce dog food and cat food
Abstract factory - pet factory
Concrete factory = dog factory and cat factory
Abstract product
Concrete product - dog and dog food AND cat and cat food
***Implemented without inheritence because of dynamically typed nature of 
python - abstract classes not required***
abstract factory is related to factory methods and concrete factory are usually singletons
""" 

class Dog():
	"""
	One of the objects to be returned
	"""
	def __init__(self):
		pass

	def speak(self):
		return "Bark"

	def __str__(self):
		return "Dog"

class Dog_Factory():
	"""
	Concrete factory
	"""
	def get_pet(self):
		"""
		Return a Dog object
		"""
		return Dog()

	def get_food(self):
		"""
		Retuns a Dog Food object - str obj
		"""
		return "Dog Food"


class Cat():
	"""
	One of the objects to be returned
	"""
	def __init__(self):
		pass

	def speak(self):
		return "Meow"

	def __str__(self):
		return "Cat"

class Cat_Factory():
	"""
	Concrete factory
	"""
	def get_pet(self):
		"""
		Return a Cat object
		"""
		return Cat()

	def get_food(self):
		"""
		Retuns a Cat Food object - str obj
		"""
		return "Cat Food"

class Pet_Store():
	"""
	PetStore houses our Abstract Factory instance
	"""
	def __init__(self, pet_factory=None):
		"""
		Pet factory is our abstract factory
		"""
		# attribute
		self._pet_factory = pet_factory

	def show_pet(self):
		"""
		Utility method to display the details of the objects returned
		by the DogFactory
		"""
		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("Our pet is {}".format(pet))
		print("Our pet says hello by {}".format(pet.speak()))
		print("It's food is {}".format(pet_food))

# Create a concrete Factory (instantiation)
factory = Dog_Factory()
cat_factory = Cat_Factory()

# Create a pet store housing our abstract factory
shop = Pet_Store(factory)
shop2 = Pet_Store(cat_factory)

# invoke the utility method to show details of pet
shop.show_pet()
print
shop2.show_pet()
