# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # DFS
        # if not root:
        #     return 0
        # elif not root.left and not root.right:
        #     return 1
        # elif not root.left and root.right:
        #     return 1 + self.minDepth(root.right)
        # elif root.left and not root.right:
        #     return 1 + self.minDepth(root.left)
        # else:
        #     return min(1 + self.minDepth(root.left),1 + self.minDepth(root.right))
        
        
        
        #BFS
#         if not root:
#             return 0
#         lvl = 1
#         queue = [(root,1)]
#         while queue != []:
#             target = queue[0]
            
#             if target[0].left:
#                 queue.append((target[0].left,target[1]+1))
                
#             if target[0].right:
#                 queue.append((target[0].right,target[1]+1))

#             if not target[0].left and not target[0].right:
#                 return target[1]
            
#             queue.pop(0)
            
            
        return 
