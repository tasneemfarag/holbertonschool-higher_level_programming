import threading

class StrLengthThread(threading.Thread):
	
	'''Class attributes'''
	total_str_length = 0

	'''Constructor'''
	def __init__(self, word):
		threading.Thread.__init__(self)
		if not isinstance(word, str):
			raise Exception("word is not a string")
		self.__word = word


	'''public method'''
	def run(self):
		StrLengthThread.total_str_length = StrLengthThread.total_str_length + len(self.__word)
		return StrLengthThread.total_str_length