import urllib2
import urllib
import json

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token aa691ecddbb46f017092bdb87a3c55300bd33e9d'
}

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'
req = urllib2.Request(url, None, request_headers)
response = urllib2.urlopen(req)
the_page = response.read()
parsed_json = json.loads(the_page)

for i in parsed_json['items']:
	print i['full_name'] 





