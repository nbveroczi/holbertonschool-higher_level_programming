#!/usr/bin/python

import urllib2
import json

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 42ee520bd99c8951da18894d2e0cd0c06d957089'
}

def printResults(data):
    theJSON = json.loads(data)
    for item in theJSON["items"]:
        print item["full_name"]

def main():
    gitData = "https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc"
    webUrl = urllib2.urlopen(gitData)
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print "uh oh!"

if __name__ == "__main__":
  main()
