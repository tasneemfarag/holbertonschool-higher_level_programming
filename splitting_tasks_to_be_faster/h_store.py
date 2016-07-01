import threading
import time
import random

class Store(threading.Thread):

	'''Class Attributes'''
	nbpersoninside = 0	

	'''Constructor'''
	def __init__(self, item_number, person_capacity):
		threading.Thread.__init__(self)
		self.__item_number  = item_number
		self.__personal_capacity = person_capacity
		self.__fatakat = threading.BoundedSemaphore(value=person_capacity)

	'''public method'''
	def enter(self):
		self.__fatakat.acquire()
		Store.nbpersoninside = Store.nbpersoninside + 1


	'''public method'''
	def buy(self):
		#print random.randint(5, 10)
		time.sleep(random.randint(5, 10))
		bought = False
		if self.__item_number > 0 :
			self.__item_number = self.__item_number - 1
			bought = True
		Store.nbpersoninside = Store.nbpersoninside	- 1
		self.__fatakat.release()
		return bought
