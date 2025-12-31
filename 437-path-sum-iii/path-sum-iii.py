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
        :rtype: int
        """

        prefixSum = {0:1}
        self.counter = 0

        def dfs(root, currSum):
            if not root:
                return
            
            currSum += root.val
            diff = currSum - targetSum
            self.counter += prefixSum.get(diff, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)
            
            dfs(root.left,  currSum)
            dfs(root.right, currSum)
            prefixSum[currSum] -= 1
            
        
        dfs(root, 0)
        
        return self.counter