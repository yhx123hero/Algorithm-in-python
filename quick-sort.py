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

def partition(L,p,r):
	s = L[r]
	i = p-1
	for j in range(p,r):
			if compare(L[j],s):
				i = i+1
				x = L[j]
				L[j] = L[i]
				L[i] = x
	x = L[i+1]
	L[i+1] = L[r]
	L[r] = L[i+1]
	return i+1


def quicksort(L,p,r):
	if p<r:
		q = partition(L,p,r)
		quicksort(L,p,q-1)
		quicksort(L,q+1,r)
	

fin = open("input_strings.txt","r")
L = []
for eachline in fin:
	line = eachline.strip().decode('utf-8', 'ignore')
	L.append(line)
fin.close()
quicksort(L,0,8)
fout = open('quicksort.txt', 'w') 
for i in range(0,9):
	str = L[i]
	fout.write(str.strip().encode('utf-8') + '\n')                                                         
fout.close() 
