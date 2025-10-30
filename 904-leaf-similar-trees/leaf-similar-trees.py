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

        self.leaves = []
        self.leaves2 = []

        def dfs(root, alist):
            if not root:
                return
            if not root.left and not root.right:
                alist.append(root.val)
            else:
                dfs(root.left, alist)
                dfs(root.right, alist)
        

        dfs(root1, self.leaves)
        dfs(root2, self.leaves2)


        return self.leaves == self.leaves2
        


