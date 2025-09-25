# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        self.list1 = []
        self.list2 = []

        def check(root, alist):
            if not root:
                return None
            if not root.left and not root.right:
                alist.append(root.val)
            check(root.left, alist)
            check(root.right, alist)
        
        check(root1, self.list1)
        check(root2, self.list2)

        return self.list1 == self.list2

