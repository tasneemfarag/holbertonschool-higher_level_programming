require 'httpclient'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token aa691ecddbb46f017092bdb87a3c55300bd33e9d'
 }  


clnt = HTTPClient.new

res = clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc', query = nil, extheaders = {})
output = File.open( "/tmp/39","w" )
    output << res
    output.close
    puts "The file was saved!"


