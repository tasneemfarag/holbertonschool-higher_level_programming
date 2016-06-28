import threading
import sys

class FibonacciThread(threading.Thread):
	'''Constructor'''
	def __init__(self, number):
		threading.Thread.__init__(self)
		if not isinstance(number, int):
			raise Exception("number is not an integer")
		self.__number = number

	'''public method'''	
	def run(self):
		a = 0
		b = 1
		for i in range(0, self.__number):
			temp = a
			a = b
			b = temp + b
		sys.stdout.write("%d => %d\n" % (self.__number, a))
				