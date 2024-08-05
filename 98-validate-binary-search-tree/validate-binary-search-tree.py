# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []

        def dfs(node):
            if not node:
                return
            if (node.left):
                dfs(node.left)
            inorder.append(node.val)
            if (node.right):
                dfs(node.right)
        
        dfs(root)

        for i in range(1, len(inorder)):
            if (inorder[i] <= inorder[i - 1]):
                return False
        
        return True
        