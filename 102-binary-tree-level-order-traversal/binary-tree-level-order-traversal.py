# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
       
        if not root: return []
        queue = deque()
        sol = []

        queue.append(root)
        #sol = [[3][9,20],[15,7]]
        #queue = [15,7]
        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            sol.append(level)
        return sol

    # def TreeNode(self, val, right, left):
    #     self.val = val
    #     self.right = right
    #     self.left = left

    # def solution(self, root):
        