#from bs4 import BeautifulSoup
#import re

#soup = BeautifulSoup(open("sample.html"))
#for hit in soup.findAll(attrs={'class' : 'bullet medialink'}):
#	print hit.contents[0].strip()

#for link in soup.findAll('a', attrs={'href': re.compile("courses/")}):
 #   print link.get('href')

from HTMLParser import HTMLParser
import urllib

base_url = 'http://ocw.mit.edu'
lec_url_list = []
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
    	if(tag == 'a'):
    		flag = 0
        	for (key,value) in attrs:
            		if(value == 'bullet medialink' and key == 'class'):
            			flag =1
            		if(key == 'href' and flag == 1):	
            			print "link : ",value
            			lec_url_list.append(value)
            			flag = 0

lecLinkParser = MyHTMLParser()
f = urllib.urlopen("sample.html")
lec_html = f.read()
lecLinkParser.feed(lec_html)
lecLinkParser.close()

videoLinkParser = MyHTMLParser()
g = urllib.urlopen("video.html")
vid_html = g.read()
videoLinkParser.feed(vid_html)
videoLinkParser.close()

#print len(lec_url_list)					