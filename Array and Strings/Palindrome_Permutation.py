from collections import defaultdict

def check_pali(our_string):
	our_string=our_string.lower()
	counts=defaultdict(int)
	for letter in our_string:
		if ord(letter)>=97 and ord(letter)<=122:
			counts[letter]+=1
#printing counts loops
	middle=""
	for letter in counts:
		if middle and counts[letter]%2==1:
			return False
		elif counts[letter]%2==1:
			middle=letter
		return True
print(check_pali("Taco cat"))							