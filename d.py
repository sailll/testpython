import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

position=raw_input('enter the position:')
count=raw_input('enter the count:')
p=int(position)
c=int(count)
for i in range(c+1):
	ci=0
	print "Retrieve:",url
	tags = soup('a')
	for tag in tags:
		ci=ci+1
		if(ci==p):
			url = tag.get('href', None)
			html = urllib.urlopen(url).read()
			soup = BeautifulSoup(html)
			break