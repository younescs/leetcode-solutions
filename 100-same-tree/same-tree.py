# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        def checkTree(tree1, tree2):
            
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2:
                return False

            if tree1.val != tree2.val:
                return False

            return checkTree(tree1.left, tree2.left) and checkTree(tree1.right, tree2.right)

        return checkTree(p, q)

        
        