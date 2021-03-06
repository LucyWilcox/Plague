"""
CSV reader for the Plague project
"""
import csv
import os
import networkx as nx
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
            file = open(file_path, 'r')
            reader = csv.reader(file)
            yield reader
        except:
            print("cannot open", filename)

def make_routes_reader():
    # yields reader for each route (edge) file
    for filename in get_edge_files():
        try:
            file_path = EDGE_PATH + "/" + filename
            file = open(file_path, 'r')
            reader = csv.reader(file)
            yield reader
        except:
            print("cannot open", filename)


def make_cities():
    """
    makes dict of all cities where city_id is the key and the city object
    is the value
    """
    cities = {}
    for reader in make_cities_reader():
        next(reader) # skip header
        for row in reader:
            try:  # check types of input and cast to types
                name = str(row[0]).strip()
                lon = float(row[1])
                lat = float(row[2])
                country = str(row[3])
                city_id = int(row[6])
            except:
                pass #printing got annoying
                # print("input error, cannot properly cast type for line " + str([i for i in row]))
            else:
                pos = (lat, lon)
                if city_id not in cities:
                    city = City(name, pos, city_id, country)
                    cities[city_id] = city
    return cities

def add_routes(cities, G):
    for reader in make_routes_reader():
        next(reader) # skip header
        for row in reader:
            try:
                use = str(row[5])
                city_1_id = int(row[25])
                city_2_id = int(row[26])
            except:
                print("input error, cannot properly cast type for line " + str([i for i in row]))
            else:
                if city_1_id in cities and city_2_id in cities:
                    city_1 = cities[city_1_id]
                    city_2 = cities[city_2_id]
                    city_1.add_route(city_2, use)
                    G.add_edge(city_1_id, city_2_id)

def form_world():
    cities = make_cities()
    city_graph = nx.Graph()
    add_routes(cities, city_graph)
    city_graph.add_nodes_from(cities.keys())
    return cities, city_graph


# G = nx.Graph()
# cities = make_cities()
# add_routes(cities, G)
# print(G.node)
# print(cities)
# print(cities[2034])
# print(cities[920])
# print(cities[112])
# print(cities[639])