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

        self.leaves = []
        self.leaves2 = []

        def dfs(root):
            if not root:
                return
            if not root.left and not root.right:
                self.leaves.append(root.val)
                return
            else:
                dfs(root.left)
                dfs(root.right)
                return
        
        def dfs2(root):
            if not root:
                return
            if not root.left and not root.right:
                self.leaves2.append(root.val)
                return
            else:
                dfs2(root.left)
                dfs2(root.right)
                return

        dfs(root1)
        dfs2(root2)

        print(self.leaves)
        print(self.leaves2)


        return self.leaves == self.leaves2
        


