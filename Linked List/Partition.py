def partition(head,key):
	lessThan=Node(None)
	greaterEqual=Node(None)
	headL=lessThan
	headG=greaterEqual

	while head:
		if head.val<key:
			headL.next=head
			headL=headL.next
		else:
			headG.next=head
			headG=headG.next
		head=head.next
		
	head.next=greaterEqual
	
	return lessThan.next

#The time complexity is O(n) and the space complexity is O(1). 	
