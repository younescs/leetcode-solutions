# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        diff = 0
        def dfs(root: TreeNode) -> bool:
            nonlocal diff
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            
            diff = max(diff, abs(left - right))
            return 1 + max(left, right)
        dfs(root)
        return diff <= 1

        