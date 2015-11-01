import math

class Position:
	"Represents GPS position"
	def __init__(self, id, resource, lat, lon, speed, track, date):
		self.id = id
		self.resource = resource
		self.lat = lat
		self.lon = lon
		self.speed = speed
		self.track = track
		self.date = date


	"Distance. Usage: p.distance(q)"
	def distance_eu(self, q):
		return math.sqrt((self.lat - q.lat)**2 + (self.lon - q.lon)**2)


	"Is it in neighboorhoud with radio eps?"
	def is_neighboorhoud(self, q, eps):
		return self.distance_eu(q) < eps
