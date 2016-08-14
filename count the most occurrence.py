fn="/Users/caizhongmou/Desktop/resume.txt"
fhand =open(fn)
count = dict()
for line in fhand:
	words=line.split()
	for word in words:
		count[word]=count.get(word,0)+1
ans=sorted([(v,k) for (k,v) in count.items()])
ans.sort(reverse=True)
for i in ans[:10]:
	print i[1]