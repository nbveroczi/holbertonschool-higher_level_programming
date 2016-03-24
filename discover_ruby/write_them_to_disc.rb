require 'httpclient'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 576bcef0e6a9e47b7bbb47385326d42a630bfff6'
}
clnt = HTTPClient.new

res = clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc', query = nil, extheader = {})

output = File.open( "/tmp/47","w" )
output << res
output.close
puts 'The file was saved!'
