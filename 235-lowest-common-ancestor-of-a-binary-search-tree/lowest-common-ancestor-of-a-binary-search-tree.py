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

        bigger, smaller = (p, q) if p.val > q.val else (q, p)



        def check(root, bigger, smaller):

            if smaller.val < root.val < bigger.val or bigger.val == root.val or smaller.val == root.val:
                return root
            if bigger.val < root.val:
                return check(root.left, bigger, smaller)
            if smaller.val > root.val:
                return check(root.right, bigger, smaller)
        
        return check(root, bigger, smaller)
