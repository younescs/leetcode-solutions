# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        bigger = max(p.val, q.val)
        smaller = min(p.val, q.val)


        def check(root, bigger, smaller):

            if smaller < root.val < bigger or bigger == root.val or smaller == root.val:
                return root
            if bigger < root.val:
                return check(root.left, bigger, smaller)
            if smaller > root.val:
                return check(root.right, bigger, smaller)
        
        return check(root, bigger, smaller)
