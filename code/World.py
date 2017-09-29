from CSVReader import *
import numpy as np

class World(object):

	def __init__(self, infected_ids):
		""" Builds a world of cities.
		infected_ids: a list of city_ids to be set as infected
		"""
		self.cities = make_cities()
		add_routes(self.cities)
		self.infected = infected_ids
		for city_id in self.infected:
			city = self.cities[city_id]
			city.infect_self()
			cities[city_id] = city
			print(city.infected_timer)

	def should_infect_trade(self, dist):
		chance_to_infect = 1 - dist/1000
		return (np.random.random() < chance_to_infect)

	def should_infect_plg(self, dist):
		chance_to_infect = 1 - dist/1000
		return (np.random.random() < chance_to_infect)

	def loop(self, n):
		for _ in range(n):
			self.step()
			print([cities[i].name for i in self.infected])

	def step(self):
		current_infected = self.infected
		for city_id in current_infected:
			city = cities[city_id]
			for city2_id in city.route_trade:
				city2 = cities[city2_id]
				if not city2.is_infected:
					if self.should_infect_trade(city.route_trade[city2_id]):
						city2.infect_self()
						cities[city2_id] = city2
						self.infected.append(city2_id)

			for city2_id in city.route_plg:
				city2 = cities[city2_id]
				if not city2.is_infected:
					if self.should_infect_plg(city.route_plg[city2_id]):
						city2.infect_self()
						cities[city2_id] = city2
						self.infected.append(city2_id)

		for city_id in self.infected:
			city = cities[city_id]
			still_infected = city.heal()
			if not still_infected:
				self.infected.remove(city_id)

world = World([2582, 2580, 219, 1630, 855])
world.loop(50)