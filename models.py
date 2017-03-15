# -*- coding: UTF-8 -*-

class Profile(object):
	'User profile class'

	def __init__(self, name, telephone, company):
		self.name = name
		self.telephone = telephone
		self.company = company
		self.__likes = 0

	def like(self):
		self.__likes += 1

	def likes(self):
		return self.__likes

	@classmethod
	def generate_profiles(clazz, file_name):
		file = open(file_name, 'r')
		profiles = []
		for line in file:
			values = line.split(',')
			if(len(values) is not 3):
				raise ValueError('The must have 3 values')
			profiles.append(clazz(*values))
		file.close()
		return profiles

	def print_info(self):
		print 'Name: %s, Telephone: %s, Company: %s, Likes: %s' % (self.name, self.telephone, self.company, self.__likes)

class Profile_Vip(Profile):
	'User vip profile class'

	def __init__(self, name, telephone, company, nickname=''):
		super(Profile_Vip, self).__init__(name, telephone, company)
		self.nickname = nickname

	def credits(self):
		return super(Profile_Vip, self).likes() * 10.0
