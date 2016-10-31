class person(object):

	university = "RUC"

	def __init__(self, name = None, Id_no = None, time_in = None, time_out = None, availabity = None, category = None):
		self.name = name
		self.Id_no = Id_no
		self.time_in = time_in
		self.time_out = time_out
		self.availabity = availabity
		self.category = category

		if self.time_in == None:
			self.availabity = 'ABSENT'
		else:
			if self.time_out == None:
				self.availabity = 'Still in the compound'
			else:
				self.availabity = 'Left the compund already'

	def set_person_role(person):
		if isinstance(person, staff):
			self.role = "Observer"
			return self
		elif isinstance(person, student):
			self.role = "Voter"
			return self


class staff(person):
	def __init__(self):
		self.category = 'Working'


class student (person):
	def __init__(self):
		self.category = 'Studying'