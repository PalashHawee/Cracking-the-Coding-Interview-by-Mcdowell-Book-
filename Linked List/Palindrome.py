'''Implement a function to check if a linked list is a Palindrome'''
#We can implement this using iteration to save space

def reverseLL(head):
	prev=None
	while head:
		temp=head.next
		head.next=prev
		prev=head
		head=temp
	return prev

def palindrome(head):
	#empty Linked list is a palindrome
	if head is None:
		return True
	#finding length of the LL
	
	length=0
	cur=head
	while cur:
		length+=1
		cur=cur.next
	#finding halfway point
	if length%2==0:
		halfway=length/2
	elif length%2==1:
		halfway=length/2+1

	#reversing 2nd half
	cur=head
	for _ in range(halfway-1):
		cur=cur.next
	secondHalf=cur.next
	cur.next=None
	secondHalf=reverseLL(secondHalf)

	#ccomparing both halves
	firstHalf=head
	while firstHalf and secondHalf:
		if firstHalf.val!=secondHalf.val
			return False
		firstHalf=firstHalf.next
		secondHalf=secondHalf.next
	return True

'''Time complexity O(n) and Space complexity O(1)										