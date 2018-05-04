import threading
import sys

class StrLenThread(threading.Thread):
	
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
		StrLenThread.total_str_length = StrLenThread.total_str_length + len(self.__word)
		return StrLenThread.total_str_length

	
words = sys.argv[1].split(" ")
str_length_threads = []

StrLenThread.total_str_length = len(words) - 1
for word in words: 
    str_length_thread = StrLenThread(word)
    str_length_threads += [str_length_thread] 
    str_length_thread.start()

for t in str_length_threads: 
    t.join()

print "%d" % StrLenThread.total_str_length