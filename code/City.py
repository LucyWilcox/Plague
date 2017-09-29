""" Contains a City class for modeling epidemic spread through Europe """

from geopy.distance import vincenty

class City(object):
	""" City class which contains a dictionary of trade routes,
	a dictionary of pilgrimage routes, id, position, name, country,
	and whether or not it is infected.
	"""

	def __init__(self, name, pos, city_id, country):
		""" Initializes City class.
		name: string of city name
		pos: tuple of (lat, long)
		id: int that represents city
		country: string of country name
		"""
		self.name = name
		self.pos = pos
		self.city_id = city_id
		self.country = country

		self.is_infected = False
		self.infected_timer = 0
		self.infection_count = 0

		# Create dictionaries for pilgrimage routes and trade routes
		#  Dictionaries are of city_id : distance in km
		self.route_pil = dict()
		self.route_trade = dict()
		self.degree = 0
		self.clustering_coefficient = 0

	def __str__(self):
		""" Prints the city name """

		return self.name + ", " + self.country + "\nPilgrimage Routes:\n" + str(self.route_pil)+"\nTradeRoutes:\n"+str(self.route_trade)

	def calc_dist(self, pos):
		""" Given a different city's position, calculates
		the distance between them 'as a bird flies'.
		"""
		return (vincenty(self.pos, pos).meters)/1000

	def add_route(self, city, use):
		""" Given another city and what the connection was used for,
		passes the proper dictionary to add_to_dict, which will then
		add the city to the proper place.

		city: instance of City class
		use: string of either pil or trd
		"""
		if use is 'plg':
			self.add_to_dict(self.route_pil, city, use)
		else: self.add_to_dict(self.route_trade, city, use)

	def add_to_dict(self, route_dict, city, use):
		""" Checks to see if city is already in route_dict and adds
		it if not.
		"""
		if city.city_id not in route_dict:
			dist = self.calc_dist(city.pos)
			route_dict[city.city_id] = dist
			city.add_route(self, use) # Tries to add itself to the other city
			self.degree += 1

	def infect_self(self):
		""" Takes a single step in time, calculating the chance that it gets
		infected.
		"""
		self.is_infected = True
		self.infected_timer = 10
		self.infection_count += 1
