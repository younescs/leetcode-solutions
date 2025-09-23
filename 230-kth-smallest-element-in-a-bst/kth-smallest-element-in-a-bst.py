# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.g = k
        self.r = 0

        def find(root):
            if root == None:
                return

            find(root.left)
            self.g -=1
            if self.g == 0:
                self.r = root.val
                return
            find(root.right)
        
        find(root)
        

        return self.r

