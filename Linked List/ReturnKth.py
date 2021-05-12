#implement an algorithm to find the kth to last element of a singly linked list
class ListNode:
   def __init__(self, data, next = None):
      self.val = data
      self.next = next

def make_list(elements):
   head = ListNode(elements[0])
   for element in elements[1:]:
      ptr = head
      while ptr.next:
         ptr = ptr.next
      ptr.next = ListNode(element)

   return head

class Solution:
   def solve(self, node, k):
      klast = node
      last = node
      for i in range(k):
         last = last.next
      while last.next:
         last = last.next
         klast = klast.next
      return klast.val

ob = Solution()
l1 = make_list([5,4,6,3,4,7])
print(ob.solve(l1, 1))	

#time complexity O(n) and space O(1)		


		
		 