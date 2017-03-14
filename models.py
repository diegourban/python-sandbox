# -*- coding: UTF-8 -*-

class Profile(object):
	'User profile class'

	def __init__(self, name, telephone, company):
		self.name = name
		self.telephone = telephone
		self.company = company

	def print(self):
		print 'Name: %s, Telephone: %s, Company: %s' % (self.name, self.telephone, self.company)