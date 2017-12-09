"""
Proxy - useful when creating object that is resource intensive 
Postpone object creation as long as possible due to resource intesive nature of object creating
Find a place holder.
Scenario: Create producer class only when available because only a fixed number of producers can exist at a given time
Proxy is an artist that checks if producer becomes available for a guest.

Clients interact with proxy until resource intensive object becomes available
Proxy is responsible for creating the resource intensive objects.
Adaptor and decorator design patterns are related to proxy design pattern.
"""

import time

class Producer():
	"""
	Define the resource intesnive object to instantiate
	"""
	def produce(self):
		print("Producer is working hard")

	def meet(self):
		print("Producer has time to meet you now!")

class Proxy():
	"""
	Define the relatively less resource intensive proxy to instantiate as a middleman
	"""
	def __init__(self):
		self.occupied = False
		self.producer = None

	def produce(self):
		"""
		Check if the producer is available
		"""
		print("Artist (Proxy) is checking if the Producer is available!")

		if self.occupied is False:
			# if the producer is available create a producer object
			self.producer = Producer()
			time.sleep(2)

			# take the producer meet the guest
			self.producer.meet()

		else:
			# producer is occupied don't instantiate the producer
			time.sleep(2)
			print("Producer is busy")


# instantiate the proxy
proxy = Proxy()

# take the proxy: artist produce until producer is available
proxy.produce()
print()

# change the state to occupied
proxy.occupied = True

# take the Producer produce
proxy.produce()