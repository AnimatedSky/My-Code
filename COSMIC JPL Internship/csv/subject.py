class Impacts(object):
	def __init__(self, metadata, polygons):
		self.metadata = metadata
		self.polygons = polygons
class metadata(object):
	def __init__(self, user, time, image):
		self.user = user
		self.time = time
		self.image = image
class polygons(object):
	def __init__(self, label, value, points):
		self.label = label
		self.value = value
		self.points = points



