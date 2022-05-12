s=input()

def longgest(s):
	l=[]
	res=[]
	l[:0]=s
	c=0
	check=""
	
	while len(l)>0:
		print(c)
		if l[c] not in check:
			check+=l[c]
			c+=1
			if c==len(l) or c > len(l):
				res.append(check)
				l=[]
		else:
			l.pop(0)
			res.append(check)
			c=0
			check=""
	
	res=sorted(res, key=len)
	print(res)
	return res



longgest(s)
