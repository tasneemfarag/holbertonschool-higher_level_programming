import threading

class Sum():

	'''Class attribute'''
	sum = 0

	'''Constructor'''
	def __init__(self, nb_threads, numbers):
		if not isinstance(nb_threads, int):
			raise Exception("nb_threads is not an integer")
		self.__nb_threads = nb_threads
		if not all(isinstance(n, int) for n in numbers):
			raise Exception("numbers is not an array of integers")
		self.__numbers = numbers
		self.__sum_array_threads = []

		spliting_index = len(self.__numbers)/self.__nb_threads
		for num in range(1, self.__nb_threads + 1):
			sum_array_thread = SumThread(self.__numbers)
			self.__sum_array_threads += [sum_array_thread]
			sum_array_thread.start()

			

	'''public method'''
	def isComputing(self):
		not_finished = False
		for t in self.__nb_threads:
			if t.is_alive():
				not_finished = True
				break
		return not_finished

	'''Public Method'''
	def __str__(self):
		return '%s' % self.sum	


class SumThread(threading.Thread):

	'''Constructor'''
	def __init__(self, numbers):
		threading.Thread.__init__(self)
		if not all(isinstance(n, int) for n in numbers):
			raise Exception("numbers is not an array of integers")
		self.__numbers = numbers	

	'''public method'''
	def run(self):
		Sum.sum = sum(self.__numbers)
		return Sum.sum

