# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:

        if not root:
            return root
        queue = deque([root])

        while queue:
            node = queue.popleft()
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        return root
        



        