# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
    #pointer method
#         while head != None and head.val == val:
#             head = head.next
#         #handle middle
#         cur = head
#         while cur != None and cur.next != None:
#             if cur.next.val == val:
#                 k = cur.next.next
#                 while k != None and k.val == val:
#                     k = k.next
#                 cur.next = k
#             cur = cur.next
#         return head
        
        
        #dummy node method
        t = ListNode(0)
        t.next = head
        cur, prev = head, t

        
        while cur != None:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return t.next

    
        
