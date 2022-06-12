"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':


        memo = {}

        def dfs(node):

            if node in memo:
                return memo[node]

            copy = Node(node.val)
            memo[node] = copy

            for neighbor in node.neighbors:
                _neighbors = dfs(neighbor)
                copy.neighbors.append(_neighbors)

            return copy

        if node:
            return dfs(node)

        return None










        '''# T O(n) M O(n)

        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node) if node else None'''
