# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0
        if not root:
            return diameter

        def traverse(node):
            nonlocal diameter
            
            if (not node):
                return 0

            if (not node.left and not node.right):
                return 1
            
            left = traverse(node.left)
            right = traverse(node.right)
            diameter = max(diameter, left + right)

            return max(left, right) + 1
        
        traverse(root)
        return diameter