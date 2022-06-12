# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # dfs - recursive
        def dfs(node, sum):

            if not node:
                return False

            sum += node.val

            # if leaf node and sum == target return true
            if not node.left and not node.right and sum == targetSum:
                return True

            l = dfs(node.left, sum)
            r = dfs(node.right, sum)

            return l or r


        return dfs(root, 0)
