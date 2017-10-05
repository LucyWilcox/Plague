from CSVReader import *
import numpy as np
import networkx as nx
import random


class World():

	def __init__(self, cities, city_graph, infected_ids, transmission, percent_quarantine=0):
		""" Builds a world of cities.
		infected_ids: a list of city_ids to be set as infected
		"""
		# self.cities = make_cities()
		# self.city_graph = nx.Graph()
		# add_routes(self.cities, self.city_graph)
		# self.city_graph.add_nodes_from(self.cities.keys())
		self.cities = cities.copy()
		self.city_graph = city_graph.copy()
		self.cant_infect = []
		self.assign_values()
		self.infected = infected_ids
		self.transmission = transmission
		self.total_infections = 1
		self.num_cities_infected = 1
		self.percent_quarantine = percent_quarantine
		# self.step_count = 0

		self.quarantine_cities()

		for city_id in self.infected:
			if city_id not in self.cant_infect:
				city = self.cities[city_id]
				city.is_infected = True
				# city.infected_timer = 5
				city.infection_count += 1
				self.cities[city_id] = city

	def quarantine_cities(self):
		num_remove = self.percent_quarantine * len(self.cities)
		for key in random.sample(self.cities.keys(), int(num_remove)):
			self.cant_infect.append(key)
			self.city_graph.remove_node(key)
			del self.cities[key]

	def quarantine_hub_cities(self):
		hub_cities = [city_id for city_id in self.cities if self.cities[city_id].degree > 6]
		num_remove = self.percent_quarantine * len(hub_cities)
		for city_id in random.sample(hub_cities, int(num_remove)):
			self.cant_infect.append(city_id)
			self.city_graph.remove_node(city_id)
			del self.cities[city_id]

	def should_infect_trade(self, dist):
		""" Calculates the likelihood something should be infected based on transmission,
		distance, and susceptibility. """
		chance_infect = np.min([250/(dist+1), 1]) * self.transmission
		tossing = np.random.choice([1, 0], p=[chance_infect, 1 - chance_infect])
		if tossing == 1:
			return True
		return False

	def should_infect_plg(self, dist):
		# chance_infect = np.min([250/(dist+1), 1]) * self.transmission
		chance_infect = self.transmission
		tossing = np.random.choice([1, 0], p=[chance_infect, 1 - chance_infect])
		if tossing == 1:
			return True
		return False

	def loop(self, max_steps):
		""" Runs until either the total infections have exceeded 6 times the number
		of cities OR the maximum number of steps has been reached. """
		for _ in range(max_steps):
			self.step()
			
		return self.infected

	def step(self):
		""" Steps through and tries to infect the neighbors of all infected cities. """
		current_infected = self.infected
		infected_this_step = []

		for city_id in current_infected:
			if city_id not in self.cant_infect:
				city = self.cities[city_id]
				for city2_id in city.route_trade:
					if city2_id not in infected_this_step and city2_id not in self.cant_infect:
						city2 = self.cities[city2_id]
						if self.should_infect_trade(city.route_trade[city2_id]):
							infected_this_step.append(city2_id)
							self.cities[city2_id] = self.infect_city(city2)

				for city2_id in city.route_plg:
					if city2_id not in infected_this_step and city2_id not in self.cant_infect:
						city2 = self.cities[city2_id]
						if self.should_infect_trade(city.route_plg[city2_id]):
							infected_this_step.append(city2_id)
							self.cities[city2_id] = self.infect_city(city2)

		# for city_id in self.infected:
		# 	city = self.cities[city_id]
		# 	has_healed = city.heal()
		# 	if has_healed:
		# 		self.infected.remove(city_id)
		# 		print(city.name + " has healed.")
		# 	self.cities[city_id] = city

		# self.step_count+=1

	def infect_city(self, city_to_infect):
		""" Updates all the pieces of infecting a city """
		city_to_infect.infection_count += 1
		# city_to_infect.infected_timer += 5
		self.total_infections += 1
		if not city_to_infect.is_infected:
			city_to_infect.is_infected = True
			self.infected.append(city_to_infect.city_id)
			self.num_cities_infected += 1
		return city_to_infect

	def closeness(self, city_id):
		city = self.cities[city_id]
		city.closeness = nx.closeness_centrality(self.city_graph, city_id)
		self.cities[city_id] = city

	def clustering_coefficient(self, city_id):
		city = self.cities[city_id]
		city.clustering_coefficient = nx.clustering(self.city_graph, city_id)
		self.cities[city_id] = city

	def assign_values(self):
		for city_id in self.cities:
			if city_id not in self.cant_infect:
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
# cities, city_graph = form_world()

# for _ in range(10):
# 	starting_city = np.random.choice(starting_cities)
# 	percent_quarantine = .30
# 	world = World(cities, city_graph, [starting_city], 0.15, percent_quarantine)
# 	print(world.cant_infect)
# 	infected = world.loop(100)
# 	print(len(infected))

#starting_cities = [477, 689,742,767,769,770, 814,909,988,1009,1028,1029,1034,1093,1105,1161,1167,1206,120, 7]
#starting_city = np.random.choice(starting_cities)
#cities, city_graph = form_world()
#percent_quarantine = .15
#world = World(cities, city_graph, [starting_city], 0.15, percent_quarantine)
#print(world.cant_infect)
#infected = world.loop(100)
#print(len(infected))

# # infected = world.loop(50)
# print(len(infected))
# # print(infected)
# # print(world.closeness(1097))

# closeness, clustering_coefficient, degree, infection_count = grapher(world.cities)

# # print(clustering_coefficient)
# # print(closeness)
# # print(degree)
# # print(infection_count)
# print(sum(infection_count)/float(sum(degree)))