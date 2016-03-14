a=2
def p():
	for i in range(1,10):
		print i

p()
def poi(a,b):
    for i in range(a,b):
    	print i
a=input("please enter the value of a\n")
b=input("please enter the value of b\n")
poi(a,b)
import time
t=time.localtime()
print "asctime is %s"%time.asctime(t)
