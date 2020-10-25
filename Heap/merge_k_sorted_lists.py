# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #use a heap
        import heapq
        
        dummy = ListNode(0)
        cur = dummy
        l = []
        
        #create lists of n values
        for k in lists:
            head = k
            while head != None:
                l.append(head.val)
                head = head.next
                
        #create heap
        heapq.heapify(l)
        
        #add all our values from our heap
        while l:
            cur.next = ListNode(heapq.heappop(l))
            cur = cur.next
        return dummy.next
        

            
            

        
