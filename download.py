from HTMLParser import HTMLParser
import urllib
import os

base_url = 'http://ocw.mit.edu'
lec_url_list = []
video_url_list = []

class lecHTMLParser(HTMLParser):
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

class vidHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		if(tag == 'a'):
			for (key,value) in attrs:
				if(value[:22] == 'http://www.archive.org' and key == 'href'):
					print "link : ",value
					video_url_list.append(value)
				break

lecLinkParser = lecHTMLParser()
f = urllib.urlopen("sample.html")
lec_html = f.read()
lecLinkParser.feed(lec_html)
lecLinkParser.close()

videoLinkParser = vidHTMLParser()
g = urllib.urlopen("video.html")
vid_html = g.read()
videoLinkParser.feed(vid_html)
videoLinkParser.close()
