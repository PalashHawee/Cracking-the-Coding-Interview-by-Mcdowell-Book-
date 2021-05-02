#given two strings write a method to decide if one is permutation of the other

def permutation(str1,str2):
	n1=len(str1)
	n2=len(str2)
	#checking if the strings are at the same length
	if(n1!=n2):
		return False
	#sorting strings
	a=sorted(str1)
	str1=" ".join(a)
	b=sorted(str2)
	str2=" ".join(b)

	#comparing sorted strings
	for i in range(0,n1,1):
		if(str1[i]!=str2[i]):
			return False
	return True	

if __name__ == '__main__':
	str1='Palash'
	str2='Palash'
	if(permutation(str1,str2)):
		print ('Yes')
	else:
		print('No')		