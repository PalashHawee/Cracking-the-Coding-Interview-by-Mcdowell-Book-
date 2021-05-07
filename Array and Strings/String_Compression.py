
def string_compression(input_str):
	cmp_str=""
	count=1
	for i in range(len(input_str)-1):
		if input_str[i]==input_str[i+1]:
			count+=1
		else:
			cmp_str+=input_str[i]+str(count)
			count=1
	cmp_str+=input_str[i]+str(count)
	if len(cmp_str)>len(input_str):
		return input_str
	else:
		return cmp_str
input_str_test="aabcccccaaa"
string_compression(input_str_test)
print(string_compression(input_str_test))				