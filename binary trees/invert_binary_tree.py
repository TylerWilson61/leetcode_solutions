# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if not root:
            return root
      
        queue = [root]
        while queue != []:
            target = queue.pop()
            left = target.left
            target.left = target.right
            target.right = left
            if target.right:
                queue.append(target.right)
            if target.left:
                queue.append(target.left)
                
        return root
                
            
        
