#write an algorithm such that if an element in an M*N matrix is 0,its entire row and coulm set to 0
def zeroMetrix(metrix):
	for r in range(len(matrix)):
		for c in range(len(matrix[r]):
			if matrix[r][c]==0:
				setNone(matrix,r,c)
	for r in range(len(matrix)):
		for c in range(len(matrix[r])):
			if matrix[r][c]==None:
				matrix[r][c]=0
def setNone(matrix,r,c):
	#set the row to none
	for i in range(len(matrix[r])):
		if matrix[r][i]!=0:
			matrix[r][i]=None
	#set column to none
	for i in range(len(matrix[r])):
		if matrix[i][c]!=0:
			matrix[i][c]=None
	matrix[r][c]=None							
													