'''You have two numbers represented by a linked list, where each node contains a single digit.
the digits are stored in reverse order, such that the 1's digit is at the head of the list.
write a function that adds the two numbers and returns the sum as a linked list'''

class Node:
	def __init__(self,val):
		self.val=val
		self.next=None
def sumList(l1,l2):
	sumList=Node(None)
	cur=sumList
	carryOver=False

	while l1 or l2 or carryOver:
		newNode=Node(0)

		if l1:
			newNode.val+=l1.val
			l1=l1.next
		if l2:
			newNode.val+=l2.val
			l2=l2.next

		if newNode.val>9:
			carryOver=True
			newNode.val-=10

		cur.next=newNode
		cur=cur.next
	return sumList.next
#Time complexity O(n), space complexity O(n)							
