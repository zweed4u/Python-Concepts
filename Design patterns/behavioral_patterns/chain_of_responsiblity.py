"""
Chain of responsibility - 
decouples request and its processing
Scenario - receieve integer use handlers to find out its range
Abstract handler - store successor who will handle request if it is not handled at current handler
Concrete handler - checks if it can handle the request and return True if the request was handled
Composite is related to the chain of responsibility design pattern
"""

class Handler():
	# abstract handler
	def __init__(self, successor):
		# define who is the next handler
		self._successor = successor

	def handle(self, request):
		handled = self._handle(request) # if handled, stop here

		# otherwise, keep going
		if handled is not True:
			# use successor
			self._successor.handle(request)

	def _handle(self, request):
		raise NotImplementedError("Must provide implementation in subclass")


class ConcreteHandler1(Handler):
	# inherit from the abstract handler class
	# concrete handler 1
	def _handle(self, request):
		if 0 < request <= 10:
			# provide a condition for handling
			print("request {} handled in handler 1".format(request))
			return True # indicates that the request has been handled


class DefaultHandler(Handler):
	# inherit from the abstract handler class
	# default handler
	def _handle(self, request):
		# if there is no handler available
		# no condition checking since this is the default handler
		print("End of chain, no handler for {}".format(request))
		return True # indicate that the request has been handled


class Client():
	# using handlers
	def __init__(self):
		# create handlers and use them in a sequence you want
		# default handler has no successor
		self.handler = ConcreteHandler1(DefaultHandler(None))

	def delegate(self, requests):
		# send your requests one at a time for handlers to handle
		for request in requests:
			self.handler.handle(request)


# create a client
client = Client()

# create requests
requests = [2, 5, 30]
 
# send the request
client.delegate(requests)
