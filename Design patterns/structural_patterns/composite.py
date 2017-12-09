"""
Composite design pattern maintains tree data structure to represent part-whole relationships.
Create recursive tree data structure so that element of tree can have its own subelements 
eg. menu > sub-menu > sub-sub-menu
Solution consists of 3 elements: 
component - abstract class
child - concrete class inherits from component
composite - concrete class inherits from component (maintains child objects by adding and removing them to a tree data strucutre)
Decorator, iterator and visitor are related to composite design pattern
"""

class Component():
	# abstract class - define interfacing method component_function
	def __init__(self, *args, **kwargs):
		pass

	def component_function(self):
		pass

class Child(Component): #inherits from the abstract class - component
	# concrete class
	def __init__(self, *args, **kwargs):
		super().__init__(self, *args, **kwargs)

		# this is where we store the name of the child item - get 1st argument of instantiation process of child
		self.name = args[0]

	def component_function(self):
		# print the name of the child
		print("{}".format(self.name))

class Composite(Component): #inherits from the abstract class - component
	# concrete class and maintains the ree recursive structure
	def __init__(self, *args, **kwargs):
		super().__init__(self, *args, **kwargs)

		# this is where we store the composite object - 1st argument to get name of the composite object
		self.name = args[0]

		# this is where we keep our child items in the composite object
		self.children = []


	#utility methods
	def append_child(self, child):
		# method to add a new child item
		self.children.append(child)

	def remove_child(self, child):
		# method to remoca a child item
		self.children.remove(child)

	def component_function(self):

		# print the name of the composite object
		print("{}".format(self.name))

		# iterate through the child objects and invoke their component function printing their names
		for child in self.children:
			child.component_function()

# build a composite sub-menu 1 - not top level
sub1 = Composite("sub-menu1")

# create a new child sub-sub-menu 11 
subsub11 = Child("sub-sub-menu11")

# create a new child sub-sub-menu 12
subsub12 = Child("sub-sub-menu12")

# add the sub-sub-menu 11 to sub-menu1
sub1.append_child(subsub11)

# add the sub-sub-menu 12 to sub-menu1
sub1.append_child(subsub12)

# build a top level composite menu
top = Composite("top_menu")

# build a sub-menu2 that is not a composite
sub2 = Child("sub-menu2")

# add the composite sub-menu1 to the top level composite menu
top.append_child(sub1)

# add the plain sub-menu2 to the toplevel composite menu
top.append_child(sub2)

# lets test if the composite pattern works
top.component_function()
