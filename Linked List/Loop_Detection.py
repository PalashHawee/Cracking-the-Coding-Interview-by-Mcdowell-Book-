#Detecting loop in a circular linked list
def detection(head):
	slow,fast=slow.next,fast.next.next

	while fast and fast.next:
		slow=slow.next
		fast=fast.next.next
		if slow==fast
			return slow

#Time complexity O(n) and space complexity O(1)