a=open('que.aln','r')
ar=a.readlines()
numseq=len(ar)
out=open('que_que.aln','w')
for i in range(numseq):
	i=str(i)
	if i=='0':
		j='que'
	else:
		j=i
	out.write('>'+str(j)+'\n'+str(ar[int(i)].strip())+'\n')
