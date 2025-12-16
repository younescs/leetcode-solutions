# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        self.counter = 0
        def search(root, asum, tsum):
            if not root:
                return
            asum += root.val
            if asum == tsum:
                self.counter +=1
            search(root.left, asum, tsum)
            search(root.right, asum, tsum)

        def traversal(root, asum, tsum):
            if not root:
                return
            search(root, asum, tsum)
            traversal(root.left, asum, tsum)
            traversal(root.right, asum, tsum)
        

        traversal(root, 0, targetSum)
        return self.counter


        