#!/usr/bin/env python
import math

'''Class'''
class Circle():
	'''Constructor'''
	def	__init__(self, radius):

		'''Private attribute'''

		self.__radius = radius
		self.__center = [0, 0]
		self.__color = ""

		'''Public attribute'''
		self.name = ""
		
	'''Getter'''
	def get_color(self):
		return self.__color

	def get_center(self):
		return self.__center

	'''Setter'''
	def set_color(self, color):
		self.__color = color

	def set_center(self, center):	
		self.__center = [0, 0]

	'''Public method'''
	def area(self):
		return 	math.pi * self.__radius ** 2
'''
for test only
c = Circle(4)
c.set_center([0, 0])
c.set_color("Yellow")
c.name = "Sun"
print "Area of %s is %f" % (c.name, c.area())
'''