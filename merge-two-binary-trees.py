# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(t1, t2):
            if not t1 and not t2:
                return None

            t = TreeNode()

            if t1 and t2:
                t.val = t1.val + t2.val
            elif t1 and not t2:
                t.val = t1.val
            elif t2 and not t1:
                t.val = t2.val


            t.left = dfs(t1.left if t1 else None, t2.left if t2 else None)
            t.right = dfs(t1.right if t1 else None, t2.right if t2 else None)

            return t


        return dfs(root1, root2)
