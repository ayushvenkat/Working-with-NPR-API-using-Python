from urllib2 import urlopen
from json import load, dumps

#The API Key is stored in a separate  text file called apiKey.
#Access that file, and store the contents into a variable called key

fileName="apiKey.txt"
file=open(fileName,"r")
key=file.readlines()
key.strip('\n')

url = 'http://api.npr.org/query?apiKey=' 
url = url + key
url += '&numResults=1&format=json&id=1007&requiredAssets=text,image,audio' #1007 is science

response = urlopen(url)
json_obj = load(response)

for story in json_obj['list']['story']:
	print "TITLE: " + story['title']['$text'] + "\n"
	print "DATE: " + story['storyDate']['$text'] + "\n"
	print "TEASER: " + story['teaser']['$text'] + "\n"
	if 'byline' in story:
	    print "BYLINE: " + story['byline'][0]['name']['$text']+ "\n"
	
	if 'show' in story:
	    print "PROGRAM: " + story['show'][0]['program']['$text'] + "\n"
	print "NPR URL: " + story['link'][0]['$text'] + "\n" 
	print "IMAGE: " + story['image'][0]['src'] + "\n"
	if 'caption' in story:
	    print "IMAGE CAPTION: " + story['image'][0]['caption']['$text'] + "\n"
	if 'producer' in story:
	    print "IMAGE CREDIT: " + story['image'][0]['producer']['$text'] + "\n"
	print "MP3 AUDIO: " + story['audio'][0]['format']['mp3'][0]['$text'] + "\n"

for paragraph in story['textWithHtml']['paragraph']:
    print paragraph['$text'] + "\n"
