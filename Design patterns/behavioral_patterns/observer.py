"""
Observer - establishes 1 to many relationship between subject and multiple observers
subject object needs to be monitored and observers need to be notified when there is a change in the subject
Scenario - keep track of reactors core temperatures at a power plant - when there is a change in the core temperature
registered observers miust be notified. 
Solution 
subject - abstract class which has interfaces that allow for de/attaching observers and notifying observers
concrete subject classes inheriting from abstract subject class 
Singleton is related to observer design pattern
"""

class Subject():
	#represents what is being observered
	def __init__(self):
		# this is where references to all the observers are being kept
		# note that this is a one-to-many relationship and there will be one subject to be observed by multiple observers
		self._observers = []

	def attach(self, observer):
		# if the observer is not already in the observer list append the observer to the list
		if observer not in self._observers:
			self._observers.append(observer)

	def detach(self, observer):
		# simply remove the observer
		try:
			self._observers.remove(observer)
		except:
			pass

	def notify(self, modifier=None):
		# for all the observers in the list
		# dont notify the observer who is actually updating the termperature
		# update the observers
		for observer in self._observers:
			if modifier != observer:
				observer.update(self)


class Core(Subject): # inherits from subject abstract class
	def __init__(self, name=""):
		super().__init__()
		self._name = name # set the name of the core
		self._temp = 0 # initialize the core temperature to 0

	@property 
	def temp(self):
		# getter for the temperature attribute
		return self._temp

	@temp.setter
	def temp(self, temp):
		# setter for the temperature attribute
		self._temp = temp
		# notify the observers whenever somebody changes the core temperature
		self.notify()

class TempViewer():
	def update(self, subject):
		# alert method that is invoked when the notify() method in the concrete subject is invoked
		print("Temperature Viewer: {} has temperature {}".format(subject._name, subject._temp))

# create subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

# create observers
v1 = TempViewer()
v2 = TempViewer()

# attach observers to c1
c1.attach(v1)
c1.attach(v2)

# change temp of c1
c1.temp = 80
c1.temp = 90
