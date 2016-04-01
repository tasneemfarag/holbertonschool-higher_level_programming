import urllib2
import urllib

request_headers = {
 'User-Agent': 'Holberton_School',
 'Authorization': 'token aa691ecddbb46f017092bdb87a3c55300bd33e9d'
}  

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'
req = urllib2.Request(url, None, request_headers)
response = urllib2.urlopen(req)
the_page = response.read()



file = open('/tmp/39', 'w+')
file.write(the_page)
file.close

print "The file was saved!"