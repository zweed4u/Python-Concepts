"""
Adapter converts the inerface of a class into another one a client is expecting
Incompatible interfaces between a client and a server
Scenario - Korean and British objects that have different speak methods - instead the client
wants a uniform speak method
Adapter solution translates the method names between the client and the server code
Bridges and decorators are related to the adapter design pattern
"""

class Korean():
	# Korean speaker
	def __init__(self):
		self.name = "Korean"

	def speak_korean(self):
		return "An-neyong?"

class British():
	# English speaker
	def __init__(self):
		self.name = "British"

	# different method name here
	def speak_english(self):
		return "How are you?"

class Adapter():
	"""
	This changes the generic method name to individualized names
	"""
	def __init__(self, object, **adapted_method):
		self._object = object

		# Add a new dictionary ite that establishes the mapping between the generic method name: speak() and the concrete method
		# eg. speak() will be translated to speak_korean() if the mapping says so
		self.__dict__.update(adapted_method)

	def __getattr__(self, attr):
		# Simply return the rest of the attributes
		return getattr(self._object, attr)

# list to store speaker objects
objects = []

# create korean object
k = Korean()

# create british object
b = British()

# append the objects to the objects array
# but we want to change mapping between the genric speak to individualized message name
objects.append(Adapter(k, speak=k.speak_korean))
objects.append(Adapter(b, speak=b.speak_english))

for obj in objects:
	print("{} says {}\n".format(obj.name, obj.speak()))
