# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:

        def construct(preorder, inorder):

            if not preorder or not inorder:
                return
            
            node = TreeNode(preorder[0])

            mid = inorder.index(node.val)
            node.left = construct(preorder[1:1 + mid], inorder[:mid])
            node.right = construct(preorder[1+mid:], inorder[mid + 1:])

            return node

        return construct(preorder, inorder)
        
        