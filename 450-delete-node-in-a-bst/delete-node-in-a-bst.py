# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        
        def searchTree(root, key):

            if not root:
                return root
            
            elif key > root.val:
                root.right = searchTree(root.right, key)
            
            elif key < root.val:
                root.left = searchTree(root.left, key)


            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left

                curr = root.right
                while curr.left:
                    curr = curr.left
                
                root.val = curr.val
                root.right = searchTree(root.right, root.val)
            return root

        return searchTree(root, key)