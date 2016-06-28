import threading

class ReverseStrThread(threading.Thread):

	'''Class attributes'''
	sentence = ""

	'''Constructor'''
	def __init__(self, word):
		threading.Thread.__init__(self)
		if not isinstance(word, str):
			raise Exception("word is not a string")
		self.__word = word
		
	'''public method'''
	def run(self):
		ReverseStrThread.sentence = ReverseStrThread.sentence + self.__word[::-1] + " "
		return ReverseStrThread.sentence