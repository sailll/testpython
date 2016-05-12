import urllib
import json

address=raw_input("Enter the location:")

print "Retrieving",address
url=urllib.urlopen(address)
data=url.read()
info=json.loads(data)

uc=info["comments"]
print "count:",len(uc)
sum=0
for val in uc:
	sum=sum+val["count"]
print "sum is ",sum
