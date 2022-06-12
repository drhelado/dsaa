# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        output = []

        if not root:
            return output

        # use bfs to traverse tree level by level
        queue = []
        queue.append(root)
        while queue:
            sum = 0

            # get all elements in current level (available in queue)
            # making a copy of queue to push the next level in the original queue instead of using a tmp queue
            level = len(queue)
            for i in range(level):
                n = queue.pop(0)
                sum = sum + n.val

                if n.left is not None:
                    queue.append(n.left)
                if n.right is not None:
                    queue.append(n.right)

            average = sum / level
            output.append(average)

        return output
