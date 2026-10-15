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
        #technically the first base case is not needed is our case since the subroot tree is gurateed to have at least 1 element, i just wrote it in case it could be empty for educational purposes
        #an empty subroot tree is a subtree of root, even if root is empty
        
        #this is always false, if subroot is not empty and root is, it's False, 
        if not root:
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