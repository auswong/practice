# Oct 13, 2020
# Lowest Common Ancestor of a Binary Tree 
# important note: can be one of the inputs

# save parent pointers of each node
# save ancestors of p
# iterate through ancestors of q until first in common with that of p


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return
    
    st = collections.deque()
    st.append(root)
    
    parents = {}
    parents[root] = None
    # saving parents of every node
    while st:
        curr_node = st.pop()
        if curr_node.left:
            parents[curr_node.left] = curr_node
            st.append(curr_node.left)
            
        if curr_node.right:
            parents[curr_node.right] = curr_node
            st.append(curr_node.right)
    
    # finding ancestors of p using parents map
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parents[p]
    
    while q:
        if q in ancestors:
            return q
        q = parents[q]
    return None
    
        
            