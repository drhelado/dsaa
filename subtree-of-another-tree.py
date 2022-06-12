# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # if subtree is empty, it is considered a subtree
        if not subRoot:
            return True

        # if main tree empty, return false
        # no need to check for subtree because I checked above
        if not root:
            return False

        # if trees are the same, return true
        if self.sameTree(root, subRoot):
            return True

        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)

        return (l or r)


    def sameTree(self, t1, t2):
        if not t1 and not t2:
            return True

        if not t1 or not t2 or t1.val != t2.val:
            return False

        l = self.sameTree(t1.left, t2.left)
        r = self.sameTree(t1.right, t2.right)

        return l and r
