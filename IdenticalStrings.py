def areIdentical(str1,str2):
	n1=len(str1)
	n2=len(str2)
	#checking if the length is same
	if(n1!=n2):
		return False
	#sorting the strings
	str1=sorted(str1)
	str2=sorted(str1)
	#comparing sorted strings
	for i in range(0,n1):
		if str1[i]!=str2[i]:
			return False
	return True

str1='Paul'
str2='Hawee'

#calling function
if(areIdentical(str1,str2)):
	print('Two strings are Identical')	
else:
	print('Two strings are not Identical')

	