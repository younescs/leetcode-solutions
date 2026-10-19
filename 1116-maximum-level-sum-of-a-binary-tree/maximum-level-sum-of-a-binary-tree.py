# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def maxLevelSum(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        max_sum = float('-inf')
        best_level = 1
        lvl_counter = 0

        queue = deque([root])

        while queue:
            level_sum = 0

            for i in range(len(queue)):
                level_sum += queue[0].val
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            lvl_counter += 1

            if level_sum > max_sum:
                max_sum = level_sum
                best_level = lvl_counter

        return best_level
        