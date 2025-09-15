# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        
        def isSameTree(root, root2):
            if not root and not root2:
                return True
            if not root or not root2:
                return False
            if root.val != root2.val:
                return False
            return isSameTree(root.right, root2.right) and isSameTree(root.left, root2.left)

        def checkTree(root, root2):
            if root == None:
                return False
            if root.val == root2.val and isSameTree(root, root2):
                return True
            return checkTree(root.right, root2) or checkTree(root.left, root2)
        
        return checkTree(root, subRoot)
        