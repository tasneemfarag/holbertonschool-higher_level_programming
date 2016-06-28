import threading
import sys

class OrderedArrayThread(threading.Thread):

	'''Constructor'''
	def __init__(self, number):
		threading.Thread.__init__(self)
		if not isinstance(number, int):
			raise Exception("number is not an integer")
		self.__number = number
		
	'''Public method'''
	def run(self):
		index = -1

		for num in range(0, len(OrderedArray.list)):
			if self.__number > OrderedArray.list[num]:
				index = num + 1
	
		if index == -1:
			OrderedArray.list.append(self.__number)
			#sys.stdout.write("Append: %d\n" % (self.__number))
		elif index == len(OrderedArray.list):	
			OrderedArray.list.append(self.__number)
			#sys.stdout.write("Append: %d\n" % (self.__number))
		else:
			OrderedArray.list.insert(index, self.__number)
			#sys.stdout.write("%d <= %d\n" % (index, self.__number))

class OrderedArray:

	'''Class attribute'''
	list = []

	'''Constructor'''
	def __init__(self):
		self.__num_order_threads = []
		self.number = None

	'''Public method'''
	def add(self, number):
		if not isinstance(number, int):
			raise Exception("number is not an integer")

		self.number = number
		num_order_thread = OrderedArrayThread(self.number)
		self.__num_order_threads += [num_order_thread]
		num_order_thread.start()

	'''Public method'''
	def isSorting(self):
		not_finished = False
		for t in self.__num_order_threads:
			if t.is_alive():
				not_finished = True
				break
		return not_finished

	'''Public Method'''
	def __str__(self):
		return '%s' % self.list
