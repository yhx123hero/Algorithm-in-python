def compare(str1,str2):
	a = len(str1)
	b = len(str2)
	if a>b:
		return 0
	elif a<b:
		return 1
	else:
		for i in range(0,a):
			if str1[i]<str2[i]:
				return 1
			if str1[i]>str2[i]:
				return  0
		return 1

def insertsort(L):
	for i in range(1,9):
		s = L[i]
		for j in xrange(i-1,-2,-1): 
			if j == -1:
				break
			if compare(L[j],s):
				break
			L[j+1] = L[j]
		if (j+1)!=i:
			L[j+1] = s
		

fin = open('input_strings.txt', 'r') 
L = []
for eachLine in fin: 
	line = eachLine.strip().decode('utf-8', 'ignore')
	L.append(line)
fin.close()  
insertsort(L)
fout = open('insertsort.txt', 'w') 
for i in range(0,9):
	str = L[i]
	fout.write(str.strip().encode('utf-8') + '\n')                                                         
fout.close() 
