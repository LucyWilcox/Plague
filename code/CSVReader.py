"""
CSV reader for the Plague project
"""
import csv
import os
from City import City

NODE_PATH = 'OWTRAD/nodes'
EDGE_PATH = 'OWTRAD/edges'

def get_node_files():
    # get name of each node file
    for filename in os.listdir(NODE_PATH):
        yield filename

def get_edge_files():
    # get name of each edge file
    for filename in os.listdir(EDGE_PATH):
        yield filename

def make_cities_reader():
    # yields reader for each city (node) file
    for filename in get_node_files():
        try:
            file_path = NODE_PATH + "/" + filename
            file = open(file_path, 'rb')
            reader = csv.reader(file)
            yield reader
        except:
            print("cannot open", filename)

def make_cities():
    cities = {}
    for reader in make_cities_reader():
        reader.next() # skip header
        for row in reader:
            try:  # check types of input and cast to types
                name = str(row[0]).strip()
                lon = float(row[1])
                lat = float(row[2])
                country = str(row[3])
                city_id = int(row[6])
            except:
                print("input error, cannot properly cast type for line " + str([i for i in row]))
            else:
                pos = (lat, lon)
                if city_id not in cities:
                    city = City(name, pos, city_id, country)
                    cities[city_id] = city
    print cities


make_cities()
