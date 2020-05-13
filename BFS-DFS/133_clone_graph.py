import collections
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# May 13, 2020: one pass BFS
# NEXT TIME: try 2 pass DFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        copy_node = Node(node.val, [])        
        made = {copy_node.val: copy_node}
        visited = set()
        old_q = collections.deque([node])  
        
        while old_q:
            old_node = old_q.pop()
            copy_node = made[old_node.val]
            visited.add(copy_node.val)
            for neighbor in old_node.neighbors:
                # haven't made a copy of this neighbor yet
                # make copy and link in both directions
                if neighbor.val not in made:
                    copy_neighbor = Node(neighbor.val,[copy_node])
                    copy_node.neighbors.append(copy_neighbor)
                    old_q.append(neighbor)
                    made[copy_neighbor.val] = copy_neighbor
                # made this neighbor but need to add links 
                elif neighbor.val not in visited:
                    copy_node.neighbors.append(made[neighbor.val])
                    made[neighbor.val].neighbors. append(copy_node)

        return made[1]
