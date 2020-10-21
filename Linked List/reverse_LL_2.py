# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        #create dummy
        dummy = ListNode(0,head)
        prev = dummy

        
        #establish prev, cur
        for i in range(m-1):
            prev = prev.next
        cur = prev.next

        #change pointers
        for k in range(n-m):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
  

        return dummy.next
