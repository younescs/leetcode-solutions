# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
      
        self.output = 0

        def search(root, hsf):
            if root == None:
                return
            hsf = max(hsf, root.val)
            if hsf <= root.val:
                self.output +=1
            search(root.right, hsf)
            search(root.left, hsf)

        search(root, root.val)

        return self.output