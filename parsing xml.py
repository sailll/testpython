import urllib
import xml.etree.ElementTree as ET


address = raw_input('Enter location: ')

url = address
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)


results = tree.findall('.//count')
sum=0
for result in results:
	sum=sum+int(result.text)
print sum

