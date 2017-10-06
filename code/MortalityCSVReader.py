import csv
import os
import networkx as nx
from City import City
from World import cities

MORTALITY_PATH = 'Mortality/MortalityData.csv'

def make_reader():
    try:
        file = open(MORTALITY_PATH, 'r')
        reader = csv.reader(file)
        return reader
    except:
        print("cannot open", MORTALITY_PATH)

def bla():
	reader = make_reader()
	print reader, type(reader)
	cities_mortality = {}
	mortality_data = []
	for row in reader:
		mortality_data.append(row)

	print mortality_data
	new_mortality_data = [v for v in mortality_data if type(v) is str]
	print new_mortality_data


bla()


# def add_mortality_to_city:
# 	for city_id in cities:
# 		city = cities[city_id]
# 		if city