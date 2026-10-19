# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:

        alist = []

        def dfs(root):
            nonlocal alist
            if not root:
                return

            dfs(root.left)
            alist.append(root.val)
            dfs(root.right)

        dfs(root)

        return alist[k-1]
        