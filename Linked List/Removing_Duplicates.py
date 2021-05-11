def removeDuplicates(head):
	if head is None:
		return head
	items=set()
	items.add(head.val)
	cur=head
	while cur and cur.next:
		if cur.next.val in items:
			cur.next=cur.next.next
		else:
			items.add(cur.next.val)
			cur=cur.next
	return head
#The time complexity is O(n) and the space complexity is O(n).					