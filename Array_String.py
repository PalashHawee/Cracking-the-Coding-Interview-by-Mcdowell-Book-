#Implement an Algorithm to determine if a string has all unique characters
#Brute Force approach O(n^2)

def uniqueCharacters(str):
	for i in range(len(str)):
		for j in range(i+1,len(str)):
			if (str[i]==str[j]):
				return False
	return True
str='Palash Hawee'
if(uniqueCharacters(str)):
	print("The string has",str,"similar characters")
else:
	print("The string has",str,"unique characters")

