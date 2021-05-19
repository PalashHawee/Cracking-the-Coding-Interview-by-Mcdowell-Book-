'''Given two linked list determine if the two lists intersect'''

def intersection(l1,l2):
	p1=l1
	p2=l2
	p1Switch=False
	p2Switch=False

	while (p1 or not p1Switch) and (p2 or not p2Switch):
		if p1==p2:
			return p1
		p1=p1.next
		p2=p2.next

		if p1 is None and not p1Switch:
			p1=l2
			p1Switch=True

		if p2 is None and not p2Switch:
			p2=l1
			p2Switch=True	

'''Time complexity is O(n) and space complexity O(1)				
