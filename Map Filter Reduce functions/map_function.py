"""
Map function
"""

import math
def area(radius):
	"""
	Area of circle given radius
	"""
	return math.pi*(radius**2)

# Compute areas of many circles given all of their radius'
radii = [2, 5, 7.1, .3, 10]
print(radii)

# Direct method
areas = []
for radius in radii:
	areas.append(area(radius))
print(areas)

# Map method - takes a function and iterable (list here)
# Map() applies the function given as the first arg to each element in the iterable fiven as the second arg
# Cast as list to print out as map returns iterator not data
print(list(map(area, radii)))


# Using map function on map data - celsius datapoints to farenheit
celsius_temps = [('Berlin',29),('Cairo',36),('Buenos Aires',19),('Los Angeles',26),('Tokyo',27),('New York',28),('London',22),('Beijing',32)]

# Lambda function convert tuple's temp element from celsius to farenheit
celsius_to_farenheit = lambda city_and_temp: (city_and_temp[0], (9/5)*city_and_temp[1]+32 )

# Maps the lambda function to each element in the celisus temp array
print(list(map(celsius_to_farenheit, celsius_temps)))