# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        """
        self.count = 0
        #bsf = biggest so far
        
        def dfs(root, bsf):
            if not root:
                return 
            if root.val >= bsf:
                self.count +=1
            bsf = max(root.val, bsf)
            dfs(root.left, bsf)
            dfs(root.right, bsf)
            
            
        dfs(root, root.val)
        
        return self.count
        
        
        
        
        