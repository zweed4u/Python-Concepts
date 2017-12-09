"""
Filter function
"""

# Filters out data that is not needed - eg. find all data ABOVE the average
import statistics # easy mean function see line 10

data = [1.3, 2.7, .8, 4.1, 4.3, -.1]
average = sum(data)/len(data)
assert average == statistics.mean(data)
print(average)

# Grab only points in dataset that are ABOVE average
# Filter function takes function as first arg and list of data as second arg
# Filter function will only return the data for which the 1st arg function is true

# above average
print(list(filter(lambda x: x>average, data)))

# below average
print(list(filter(lambda x: x<average, data)))



# Remove missing/empty data
countries = ['', 'Argentina', '', 'Brazil', 'Chile', '', 'Colombia', '', 'Ecuador', '', '', 'Venezuela']

# None as first arg will filter out all values of our second arg iterable that would be considered False in a boolean setting
print(list(filter(None, countries)))