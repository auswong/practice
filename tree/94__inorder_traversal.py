# Oct 13, 2020
# Binary Tree Inorder Traversal

# make helper function that takes in array as input and
# comput left, add current, compute right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorderTraversal(self, root: TreeNode) -> List[int]:
    ans = []
    compute(root, ans)
    return ans

def compute(self, root, ans):
    if not root:
        return
    
    if root.left:
        compute(root.left, ans)
    
    ans.append(root.val)
    
    if root.right:
        compute(root.right, ans)