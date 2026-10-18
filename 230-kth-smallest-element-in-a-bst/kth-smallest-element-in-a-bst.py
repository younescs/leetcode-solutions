# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        counter = k
        answer = None
        def dfs(root):
            nonlocal counter
            nonlocal answer
            if not root:
                return
            
            dfs(root.left)
            if counter <= 0:
                return
            counter -= 1
            if counter == 0:
                answer = root.val
                return
            if counter <=0: return
            dfs(root.right)
        
        dfs(root)
        return answer