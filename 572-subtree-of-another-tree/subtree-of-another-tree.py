# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class TreeNode
#     def __init__(self, val=0, right, left):
#         self.val = val
#         self.right = right
#         self.left = left

class Solution:
    def isSubtree(self, root:TreeNode | None, subroot:TreeNode | None):
        if not root and not subroot:
            return True
        if not root or not subroot:
            return False

        if root.val == subroot.val and self.is_SameTree(root, subroot):
            return True
        else:
            return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)
            


    def is_SameTree(self, q, p):
        if not q and not p:
            return True
        if not q or not p:
            return False
        if q.val != p.val:
            return False
        return self.is_SameTree(q.left, p.left) and self.is_SameTree(q.right, p.right)