# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        queue = deque([root])
        maxval = root.val
        maxlevel = 1
        currlevel = 1
        while queue:
            currsum = 0
            
            for i in range(len(queue)):
                element = queue.popleft()
                currsum += element.val
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)

            if  currsum > maxval:
                maxval = currsum
                maxlevel = currlevel

            currlevel += 1
           
            
        return maxlevel
