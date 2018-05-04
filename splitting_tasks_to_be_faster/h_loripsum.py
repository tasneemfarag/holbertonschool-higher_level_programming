import threading
import urllib2

class LoripsumThread(threading.Thread):

	'''Constructor'''
	def __init__(self, filename):
		threading.Thread.__init__(self)
		self.__filename = filename

	'''public method'''
	def run(self):	
		req = urllib2.Request('http://loripsum.net/api/1/short')
		response = urllib2.urlopen(req)
		txt = response.read()
		f = open(self.__filename, 'a')
		f.write(txt)
		#print txt
		f.close()


	#req = urllib2.Request('http://loripsum.net/api/1/short')
	#print req.
	#f = open(req)
	#data = f.read()
	#filename = write(req)
	#f.close()