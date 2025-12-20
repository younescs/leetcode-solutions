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


        self.counter = 0

        def dfs(root, currsum, targetSum, alist):
            #leaves
            if not root:
                return

            #nodes
            currsum += root.val
            if currsum == targetSum:
                self.counter +=1

            temp = currsum
            for i in alist:
                temp -= i 
                if temp == targetSum:
                    self.counter +=1
            
            alist.append(root.val)
     

            dfs(root.left, currsum, targetSum, alist)
            dfs(root.right, currsum, targetSum, alist)
            alist.pop()

        dfs(root, 0, targetSum, [])

        return self.counter

        

            
        