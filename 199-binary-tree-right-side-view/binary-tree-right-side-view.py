# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        queue = deque([root])
        
        alist = [root.val]
        while queue:
            for i in range(len(queue)):
                element = queue.popleft()
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
        
            if queue: alist.append(queue[-1].val)

        return alist

            
            
            

            
        