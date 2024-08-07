# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if (not root):
            return 0
        result = []
        queue = [root]

        while (queue):
            size = len(queue)
            level = []
            level_sum = 0
            for i in range(size):
                node = queue.pop(0)
                level_sum += node.val
                if (node.left):
                    level.append(node.left)
                if (node.right):
                    level.append(node.right)
            queue = level
            result.append(level_sum / size)

        return result

        