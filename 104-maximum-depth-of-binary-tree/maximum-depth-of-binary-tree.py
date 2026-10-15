# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        
        if not root:
            return 0
        #we need to go through every level and update the counter at each level
        #we are gonna use a queue for this

        #this is our queue of nodes:
        nodeq = deque()

        #we first add the root to it:
        nodeq.append(root)
        counter = 0
        #now we keep going as long as it's fll
        while nodeq:
            level_size = len(nodeq)
            for i in range(level_size):
                curr = nodeq.popleft()
                if curr.left:
                    nodeq.append(curr.left)
                if curr.right:
                    nodeq.append(curr.right)
            counter += 1
                

        return counter
        # [15, 7]
        #counter = 3
            

