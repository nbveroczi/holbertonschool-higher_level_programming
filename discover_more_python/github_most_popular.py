request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 42ee520bd99c8951da18894d2e0cd0c06d957089'
} 

import urllib2

def main():
  # open a connection to a URL using urllib2
  webUrl = urllib2.urlopen("https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc")  

  # read the data from the URL and print it
  data = webUrl.read()
  print data

if __name__ == "__main__":
  main()
