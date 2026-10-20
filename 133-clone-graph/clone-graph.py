"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = dict()
        def dfs(node):
            if not node:
                return None
                
            new_node = Node(node.val)
            new_node.neighbors = []
            seen[node] = new_node

            for neighbor in node.neighbors:
                if neighbor in seen:
                    new_node.neighbors.append(seen[neighbor])
                else:
                    new_node.neighbors.append(dfs(neighbor))

            
            return new_node

        return dfs(node)
        