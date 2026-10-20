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
        seen = {}
        if not node: return None

        def copy(node):
            new_node = Node()
            new_node.val = node.val
            new_node.neighbors = []
            return new_node


        first_node = copy(node)
        seen[node] = first_node
        queue = collections.deque()
        queue.append(node)

        while queue:
            curr = queue.popleft()
            list_of_neighbors = []
            for neighbor in curr.neighbors:
                if neighbor in seen:
                    list_of_neighbors.append(seen[neighbor])
                else:
                    neighbor_copy = copy(neighbor)
                    seen[neighbor] = neighbor_copy
                    list_of_neighbors.append(neighbor_copy)
                    queue.append(neighbor)
            seen[curr].neighbors = list_of_neighbors

        return first_node
                


        