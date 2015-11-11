import math
import time

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

	"String Representation"
	def toString(self):
		return "id:{0}, recurso:{1}, latitud:{2}, longitud:{3}, velocidad:{4}, orientacion:{5}, fecha:{6}".format(self.id, self.resource, self.lat, self.lon, self.speed, self.track, self.date)

	"Distance EU simple. Usage: p.distance(q)"
	def distance_eu(self, q):
		return math.sqrt((self.lat - q.lat)**2 + (self.lon - q.lon)**2)
		
	"Is it in neighboorhoud with radio eps?"
	def is_in_neighborhoodByEUSimple(self, q, eps):
		return self.distance_eu(q) < eps
		
	"Neighboorhoud EU involving speed module."
	def is_in_neighborhoodByEURelativeSpeed(self, q, eps):
		return self.distance_eu(q) < eps * self.speed
		
	"Neighboorhoud t0-reachable using distance EU and speed module."
	def is_in_neighborhoodT0Reachable(self, q, t0):
		return self.distance_eu(q) < t0 * self.speed

	"Neighboorhoud EU involving speed and orientation."
	def is_in_neighborhoodByEURelativeSpeedOrientation(self, q, eps):
		# TODO :Obtain orientation from self.orientation
		# return distance_eu(self, q) < eps * self.speed 
		return NotImplemented


	"Is it in neighboorhood by time?"
	def is_neighboorhoudByTime(self, q, lapse):
		foo = time.mktime(self.date.timetuple())
		bar = time.mktime(q.date.timetuple())
		return abs(foo - bar) < lapse


class Cluster:
	"Cluster of points, basically set of points with a center"
	def __init__(self, center, points):
		self.center = center
		self.points = points


	"String Representation"
	def toString(self):
		return "Cluster centered in: " + self.center
