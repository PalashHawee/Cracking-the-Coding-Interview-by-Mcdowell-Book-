#rotate a given matrix at 90 degree in place
def rotateMatrix(matrix):
	#Transpose the matrix
	for i in range(len(matrix)):
		for j in range(i+1,len(matrix)):
			#switching the row and column indices
			matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
	#reversing every row
	for r in range(len(matrix)):
		for i in range(len(matrix[r])/2):
		#opposite index of i
		oppIn=len(matrix[r])-1-i
		matrix[r][i],matrix[r][oppIn]=matrix[r][oppIn]	
	'''time compelexity theta(m*n) m is the number of rows and n is the
	number of colums'''
	# =(m*n)=n^2
	#space complexity is O(1) since it's being rotated only in place		