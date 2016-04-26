import re
file=raw_input("please enter the file name")
if len(file)<=1: file="/Users/caizhongmou/Desktop/apodo.txt"
fh=open(file)
l=list()
for line in fh:
	x=re.findall("[0-9]+",line)
	if len(x)!=0:
		    for k in x:
	                l.append(int(k))
print l
print len(l)
sum=0
for digit in l:
    sum=sum+long(digit); 
print sum