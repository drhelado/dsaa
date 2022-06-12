# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def recursive(preorder, inorder):
            if not preorder or not inorder:
                return None

            r = preorder[0]
            m = inorder.index(r)

            ll = preorder[1:m + 1]
            lr = inorder[:m]

            rl = preorder[m + 1:]
            rr = inorder[m + 1:]


            root = TreeNode(r)
            root.left = recursive(ll, lr)
            root.right = recursive(rl, rr)

            return root

        return recursive(preorder, inorder);
