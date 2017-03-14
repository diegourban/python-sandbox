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

	def print(self):
		print 'Name: %s, Telephone: %s, Company: %s, Likes: %s' % (self.name, self.telephone, self.company, self.__likes)
