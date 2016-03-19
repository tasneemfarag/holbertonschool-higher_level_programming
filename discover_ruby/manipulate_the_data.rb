require 'HTTPClient'
require 'json'

extheaders = {
 'User-Agent' => 'Holberton_School',
 'Authorization' => 'token 39fed9cadb8579194e82b4bc4aefa34b8fab30b7'
}


clnt = HTTPClient.new
res = clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc', query = nil, extheaders = {})
json_parse = JSON.parse(res)
array = json_parse["items"]
#puts json_parse["items"][0]["full_name"]
join_array = array.map {|a| a["full_name"]}
puts join_array.join("\n")