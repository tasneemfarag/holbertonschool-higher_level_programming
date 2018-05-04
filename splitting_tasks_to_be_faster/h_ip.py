import threading
import urllib2
import json

class IPThread(threading.Thread):

	'''Constructor'''
	def __init__(self, ip, callback):
		threading.Thread.__init__(self)
		self.__ip = ip
		self.__callback = callback

	'''public method'''
	def run(self):
		print "Search: " + self.__ip 	
		req = urllib2.Request('https://api.ip2country.info/ip?' + self.__ip)
		response = urllib2.urlopen(req)
		json_string = response.read()
		the_data = json.loads(json_string)
		country_name = the_data['countryName']
		self.__callback(country_name)
		print "countryName: " + country_name

		#f = open(self.__filename, 'a')
		#f.write(txt)
		#print txt
		#f.close()	

		#'''public method'''
	#def callback(self, country):
		#print "countryName: " + country

