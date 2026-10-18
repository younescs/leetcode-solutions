# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maximum = float('-inf')
        def dfs(root):
            nonlocal maximum
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            maximum = max(maximum, root.val + max(0,left) + max(0,right))
            return root.val + max(max(0,left), max(0,right))

        dfs(root)
        return maximum

        