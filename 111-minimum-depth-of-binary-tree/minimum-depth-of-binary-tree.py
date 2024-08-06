# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 0
        queue = [root]

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.pop(0)

                if not node.left and not node.right:
                    return depth + 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            depth +=1

        return depth


        