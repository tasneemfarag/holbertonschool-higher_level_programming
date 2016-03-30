import urllib2
import json

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token aa691ecddbb46f017092bdb87a3c55300bd33e9d'
}

r = urllib2.urlopen("https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc").read()
parsed_json = json.loads(r)

for i in parsed_json['items']:
	print i['full_name']