#Implement an Algorithm to determine if a string has all unique characters
#ASCII  O(n)

def uniqueCharacters(st):
	#using sorting
	sorted(st)
	for i in range(len(st)-1):
		if (st[i]==st[i+1]):
			return False
	return True

if __name__ == '__main__':
	st="Palash Hawee"
	if (uniqueCharacters(st)):
		print("The string has",st,"unique characters ")
	else:
		print("The string has",st,"similar characters")
		

