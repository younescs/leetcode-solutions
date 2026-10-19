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
        
        def dfs(root, maxi, mini):
            
            if not root:
                return True

            if not (mini < root.val < maxi):
                return False
            
            left = dfs(root.left, root.val, mini)
            right = dfs(root.right, maxi, root.val)
            return left and right


        return dfs(root, float('inf'), float('-inf'))

        
                        #5
                #4                  #6       
                                  #3   #7