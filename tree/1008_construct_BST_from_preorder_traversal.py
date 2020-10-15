# May 14, 2020
# Construct Binary Search Tree from Preorder Traversal

# important note: it's a BST
# the root is always the 1st element
# the root's left tree is a BST of everything less than root 
# the root's right tree is a BST of everything greater than root 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return
        
        root = TreeNode(preorder[0])
        
        i = 1
        while i < len(preorder) and preorder[i] < root.val:
            i += 1
        left = self.bstFromPreorder(preorder[1:i])
        
        right = None
        if i < len(preorder):
            right = self.bstFromPreorder(preorder[i:])
        
        root.left = left
        root.right = right
        
        return root