import urllib2

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 42ee520bd99c8951da18894d2e0cd0c06d957089'
}

def main():
  # open a connection to a URL using urllib2                                                                                                                                         
  WebUrl = urllib2.urlopen("https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc")

  # read the data from the URL and write it to a file                                                                                                                                         
  html = WebUrl.read()
  target = open("/tmp/47", "w")
  target.write(html)
  target.close()
  print "The file was saved!"

if __name__ == "__main__":
  main()
