# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        # from collections import deque
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        rstack = [[root]]
        ret = [[root.val]]
        while True:
            nxtlevel = []
            retlevel = []
            for node in rstack[-1]:
                if node.left:
                    nxtlevel.append(node.left)
                    retlevel.append(node.left.val)
                if node.right:
                    nxtlevel.append(node.right)
                    retlevel.append(node.right.val)
            if nxtlevel != []:
                rstack.append(nxtlevel)
                ret.append(retlevel)
            else:
                break
        ret.reverse()
        return ret
        
            
                
                
                
                
                
                
        return list(rstack)
        
