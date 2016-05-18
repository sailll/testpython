file="/Users/caizhongmou/Desktop/x.txt"
fh=open(file)
l=list()
for line in fh:
	s=line.lstrip()
	print s.lstrip("0123456789")
