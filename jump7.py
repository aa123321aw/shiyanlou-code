a=1
while a<100:
	a=a+1
	if(a%7==0):
		continue
	elif(a%10==7)or(a//10==7):
		continue
	print(a)
