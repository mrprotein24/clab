a=open('que.aln','r')
aR=a.readlines()

length=len(aR)
out=open('query.aln','w')
for i in range(length):
	if str(i)=='0':
		j='>que'
	else:
		j='>'+str(i)
	out.write(str(j)+'\n'+str(aR[i]))

