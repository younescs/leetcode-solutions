# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:

        
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        sol = []

        while queue:
            sol.append(queue[-1].val)
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)  

       
        return sol

#len(queue) = 1
#node:  5
#queue: []
#sol :[1, 3, 4, 5]
        #1
    #2      #3
#4

#5















#class TreeNode
    #def __init__(self, val=0, left, right):
        #self.val = val
        #self.left = left
        #self.right = right
#class Solution
    #def solution(self.root):
        #

        