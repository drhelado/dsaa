# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    output = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # dfs - recursive - bottom-up
        def dfs(node):
            # height of a null tree is -1
            # height of a leaf is 0
            if not node:
                return -1

            l = dfs(node.left)
            r = dfs(node.right)

            # find the current diameter
            d = 2 + l + r
            self.output = max(self.output, d)

            return 1 + max(l, r)

        dfs(root)

        return self.output
