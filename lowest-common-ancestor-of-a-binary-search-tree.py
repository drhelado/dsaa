# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # start pointer at root
        n = root

        # traverse tree
        while n:
            v = n.val
            pv = p.val
            qv = q.val

            # continue to one side of the tree depending on the val
            if pv > v and qv > v:
                n = n.right
            elif pv < v and qv < v:
                n = n.left
            else:
                return n
