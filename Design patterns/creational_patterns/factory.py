"""
Factory Pattern example - creational design pattern
Scenario: Pet shop - orginally sold dogs, now sell cats as well
""" 

class Cat():
	def __init__(self, name):
		self.name = name
	def speak(self):
		return "Meow"

class Dog():
	def __init__(self, name):
		self.name = name
	def speak(self):
		return "Bark"

class Fish():
	def __init__(self, name):
		self.name = name
	def speak(self):
		return "Glub glub"

def get_pet(pet="dog"):
	"""
	The factory method used to create objects 
	(Create and return object to user of the function)
	"""
	# Adding new classes/type is easy
	pets = {
		'dog': Dog("Kaiser"),
		'cat': Cat("Satan"),
		'fish': Fish("Nemo")
	}
	return pets[pet]

dog = get_pet()
print(dog.speak())

dog2 = get_pet("dog")
print(dog2.speak())

cat = get_pet("cat")
print(cat.speak())

fish = get_pet("fish")
print(fish.speak())