# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """

        TreeNode

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if val == node.val:
                return node
            elif val > node.val:
                if node.right: queue.append(node.right)
            else:
                if node.left: queue.append(node.left)


        return None
        