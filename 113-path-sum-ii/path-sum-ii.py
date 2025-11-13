# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        
        """
        self.alist = []
        
        def dfs(root, targetSum, list2):
            if not root:
                return
            list2.append(root.val)
            targetSum -= root.val
            if targetSum == 0 and not root.left and not root.right:
                self.alist.append(tuple(list2))
            dfs(root.left, targetSum, list2)
            dfs(root.right, targetSum, list2)
            list2.pop()                       
                
        dfs(root, targetSum, [])
        return self.alist
            
        