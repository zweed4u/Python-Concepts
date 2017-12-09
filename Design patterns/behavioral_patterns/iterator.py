"""
Iterator - allow client sequential access to elements of an aggregate object without exposing its underlying structure
Traversal interfaces of aggregate object get overcrowded
Scenario - build custom iterator based on zip()
only iterate up until certain point
- isolates access and traversal features of an aggregate object
- provides interface for accessing elemts of an aggregate object
- keeps track of objects being traversed
- make aggregate object, create iterator for client
composite design pattern is related to iterator design pattern
"""

def count_to(count):
	# our iterator implementation
	# our list
	deutch_numbers = [
		'eins',
		'twei', 
		'drei', 
		'vier', 
		'funf', 
		'sechs', 
		'sieben', 
		'acht'
	]

	# our built in iterator
	# creates a tuple such as (1, 'eins'),...
	iterator = zip(range(count), deutch_numbers)

	# iterate through our iterable list
	# extract the german numbers
	# put them in a generator called number
	for position, number in iterator:
		# returns a generator containing number in german
		yield number

# test the generator returned by iterator
for number in count_to(4):
	print(number)
