require 'httpclient'
require 'json'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 576bcef0e6a9e47b7bbb47385326d42a630bfff6'
}

clnt = HTTPClient.new

res = clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc', query = nil, extheader = {})

json_parse = JSON.parse(res)
array = json_parse["items"]
join_array = array.map {|a| a["full_name"]}
puts join_array.join("\n")
