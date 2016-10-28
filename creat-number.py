import numpy as np

fout = open('input_strings.txt', 'w') 
for i in range(0,9):
	num =np.random.randint(1,16)
	str = ''
	for j in range(0,num):
		str= str+chr(97 + np.random.randint(0,23))
	fout.write(str.strip().encode('utf-8') + '\n')                                                         
fout.close()      
	
