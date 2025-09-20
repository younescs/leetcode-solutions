# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        curr = root.val

        def validate(root, maxi, mini):
            if root == None:
                return True
            if not mini < root.val < maxi:
                return False
            return validate(root.left, root.val, mini) and validate(root.right, maxi, root.val)
        
        return validate(root, float('+inf'), float('-inf'))