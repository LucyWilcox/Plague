from CSVReader import *
import numpy as np
import networkx as nx

class World(object):

	def __init__(self, cities, city_graph, infected_ids, transmission):
		""" Builds a world of cities.
		infected_ids: a list of city_ids to be set as infected
		"""
		# self.cities = make_cities()
		# self.city_graph = nx.Graph()
		# add_routes(self.cities, self.city_graph)
		# self.city_graph.add_nodes_from(self.cities.keys())
		self.cities = cities
		self.city_graph = city_graph
		self.assign_values()
		self.infected = infected_ids
		self.transmission = transmission
		for city_id in self.infected:
			city = self.cities[city_id]
			city.is_infected = True
			city.infection_count += 1
			self.cities[city_id] = city

	def should_infect_trade(self, dist):
		tossing = np.random.choice([1, 0], p=[self.transmission, 1 - self.transmission])
		if tossing == 1:
			return True
		return False
		# return tossing	
		# chance_to_infect = 1 - dist/1000
		# return (np.random.random() < chance_to_infect)

	def should_infect_plg(self, dist):
		tossing = np.random.choice([1, 0], p=[self.transmission, 1 - self.transmission])
		if tossing == 1:
			return True
		return False
		# chance_to_infect = 1 - dist/1000
		# return (np.random.random() < chance_to_infect)

	def loop(self, n):
		for _ in range(n):
			self.step()
			# print([cities[i].name for i in self.infected])

		return self.infected

	def step(self):
		current_infected = self.infected
		infected_this_step = []
		for city_id in current_infected:
			city = self.cities[city_id]
			for city2_id in city.route_trade:
				if city2_id not in infected_this_step:
					city2 = self.cities[city2_id]
					if self.should_infect_trade(city.route_trade[city2_id]):
						infected_this_step.append(city2_id)
						city2.infection_count += 1
						if not city2.is_infected:
							city2.is_infected = True
							self.infected.append(city2_id)
						self.cities[city2_id] = city2

			for city2_id in city.route_plg:
				if city2_id not in infected_this_step:
					city2 = self.cities[city2_id]
					if self.should_infect_trade(city.route_plg[city2_id]):
						infected_this_step.append(city2_id)
						city2.infection_count += 1
						if not city2.is_infected:
							city2.is_infected = True
							self.infected.append(city2_id)
						self.cities[city2_id] = city2

	def closeness(self, city_id):
		city = self.cities[city_id]
		city.closeness = nx.closeness_centrality(self.city_graph, city_id)
		self.cities[city_id] = city

	def clustering_coefficient(self, city_id):
		city = self.cities[city_id]
		city.clustering_coefficient = nx.clustering(self.city_graph, city_id)
		self.cities[city_id] = city

		# for city_id in self.infected: #is this not allowing for reinfection??
		# 	city = cities[city_id]
		# 	still_infected = city.heal()
		# 	if not still_infected:
		# 		self.infected.remove(city_id)
		# 	cities[city_id] = city
	def assign_values(self):
		for city_id in self.cities:
			self.closeness(city_id)
			self.clustering_coefficient(city_id)

def grapher(cities):
	closeness = []
	clustering_coefficient = []
	degree = []
	infection_count = []
	for city in cities.values():
		closeness.append(city.closeness)
		clustering_coefficient.append(city.clustering_coefficient)
		degree.append(city.degree)
		infection_count.append(city.infection_count)

	return closeness, clustering_coefficient, degree, infection_count

# starting_cities = [477, 689,742,767,769,770, 814,909,988,1009,1028,1029,1034,1093,1105,1161,1167,1206,120, 7]
# starting_city = np.random.choice(starting_cities)
# world = World([starting_city], 0.15)
# infected = world.loop(50)
# print(len(infected))
# # print(infected)
# # print(world.closeness(1097))

# closeness, clustering_coefficient, degree, infection_count = grapher(world.cities)

# print(clustering_coefficient)
