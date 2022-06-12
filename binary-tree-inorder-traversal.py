# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        '''
        if not root:
            return []

        return  [root.val] + self.inorderTraversal(root.left) + self.inorderTraversal(root.right)
        '''

        stack = []

        out = []

        # if not root:
            # return out

        while stack or root:

            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            out.append(root.val)

            root = root.right

            '''
            print('before:', (stack))

            node = stack.pop()

            out.append(node.val)

            print('after:', (stack))

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
            '''

        return out
