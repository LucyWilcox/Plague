import csv

HUB_OUT_PATH = "hub_out.csv"
NORM_OUT_PATH = ""

def hub_out_reader():
	file = open(HUB_OUT_PATH, 'r')
	reader = csv.reader(file)
	return reader

def norm_out_reader():
	file = open(NORM_OUT_PATH, 'r')
	reader = csv.reader(file)
	return reader

def read_files(reader):
	reader.next() #skip headers
	transmition_15 = {}
	transmition_25 = {}
	transmition_50 = {}

	transmition_rate = 0.
	row = reader.next()
	while float(row[0]) == 0.15:
		transmition_rate = float(row[0])
		print transmition_rate
		row = reader.next()

	while float(row[0]) == 0.25:
		pass

	# for row in reader:
	# 	transmition_rate = row[0]
	# 	quarantine_rate = row[1]
	# 	total_infections = row[2]
	# 	cities_infected = row[3]
	# 	if transmition_rate == 0.15:



hub_reader = hub_out_reader()
read_files(hub_reader)
