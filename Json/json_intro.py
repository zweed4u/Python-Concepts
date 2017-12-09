"""
JavaScript Object Notation - small lightweight data format
"""
import os # to get path
import json
# load() load json from file
# loads() load json from string
# dump() write json data to file
# dumps() output json object as string

# Get script's path/movie_1.txt
json_file = open(f'{os.path.dirname(os.path.realpath(__file__))}/movie_1.txt', 'r', encoding='utf-8')
movie = json.load(json_file)
json_file.close()
print(type(movie))
print(movie)


# Json data formatted as a string
json_str = """
{
	"title": "Tron: Legacy",
	"composer": "Daft Punk",
	"release_year": 2012,
	"budget": 170000000,
	"actors": null,
	"won_oscar": false
}
"""
print(type(json_str))
tron = json.loads(json_str)
print(type(tron))
print(tron)


# Convert dictionary from first loaded example into valid json string
# Alloe unicode characters in string
print(type(json.dumps(movie)))
print(json.dumps(movie, ensure_ascii=False))


# Write a new object, convert to json and write to file
movie_2 = {
	'title': 'Minority Report',
	'director': 'Steven Spielberg',
	'composer': 'John Williams',
	'actors': ['Tom Cruise', 'Colin Farrell', 'Samantha Morton', 'Max von Sydow'],
	'is_awesome': True,
	'budget': 102000000,
	'cinematographer': 'Janusz Kami\u0144ski'
}
json_file_2 = open(f'{os.path.dirname(os.path.realpath(__file__))}/movie_2.txt', 'w', encoding='utf-8')
json.dump(movie_2, json_file_2, ensure_ascii=False)
json_file_2.close()
