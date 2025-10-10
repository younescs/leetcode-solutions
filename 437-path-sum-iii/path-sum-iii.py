# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        if not root:
            return 0

        def dfs(node, target):
            if not node:
                return 0
            count = 1 if node.val == target else 0
            count += dfs(node.left, target - node.val)
            count += dfs(node.right, target - node.val)
            return count

        # count paths starting from *this* node
        paths_from_root = dfs(root, targetSum)

        # then move down and repeat for all other nodes
        return paths_from_root + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
