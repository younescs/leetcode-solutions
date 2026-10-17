# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        sol = root	
        def dfs(node):
            nonlocal sol
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.val == p.val or node.val == q.val:
                if left or right:
                    sol = node
                return True
            else:	
                if left and right: 
                    sol = node
                return left or right
        dfs(root)
        return sol
