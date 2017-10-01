from CSVReader import *
import numpy as np
import pandas

class World(object):

	def __init__(self, infected_ids, transmission):
		""" Builds a world of cities.
		infected_ids: a list of city_ids to be set as infected
		"""
		self.cities = make_cities()
		add_routes(self.cities)
		self.infected = infected_ids
		self.transmission = transmission
		for city_id in self.infected:
			city = self.cities[city_id]
			city.is_infected = True
			city.infection_count += 1
			cities[city_id] = city

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
		for city_id in current_infected:
			city = cities[city_id]
			for city2_id in city.route_trade:
				city2 = cities[city2_id]
				if self.should_infect_trade(city.route_trade[city2_id]):
					city2.infection_count += 1
					if not city2.is_infected:
						city2.is_infected = True
						self.infected.append(city2_id)
					cities[city2_id] = city2

			for city2_id in city.route_plg:
				city2 = cities[city2_id]
				if self.should_infect_trade(city.route_plg[city2_id]):
					city2.infection_count += 1
					if not city2.is_infected:
						city2.is_infected = True
						self.infected.append(city2_id)
					cities[city2_id] = city2

	def closeness(self, city_id):
		city = self.cities[city_id]
		return np.sum([city.calc_dist(city2.pos) for city2 in cities.values()]) #change to graph distance



		# for city_id in self.infected: #is this not allowing for reinfection??
		# 	city = cities[city_id]
		# 	still_infected = city.heal()
		# 	if not still_infected:
		# 		self.infected.remove(city_id)
		# 	cities[city_id] = city

starting_cities = [477, 689,742,767,769,770, 814,909,988,1009,1028,1029,1034,1093,1105,1161,1167,1206,120, 7]
starting_city = np.random.choice(starting_cities)
world = World([starting_city], 0.15)
infected = world.loop(50)
print(len(infected))
# print(infected)
print(world.closeness(1097))
print(len(world.cities))
