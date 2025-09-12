# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def inversion(root):
            if root == None:
                return
            else:
                temp = root.left
                root.left = root.right
                root.right = temp
                inversion(root.left)
                inversion(root.right)

        
        inversion(root)
        return root