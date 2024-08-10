# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    # nlr
    # [8,5,1,7,10,12] 

# build the root of the tree with the value 

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        stack = []
        N = len(preorder) 
        root = TreeNode(preorder[0])
        stack.append(root)

        # if not preorder:
        #     return TreeNode(null)

        for i in range(1, N):
            # if this value is less than current node, add to the left
            if preorder[i] < stack[-1].val:
                stack[-1].left = TreeNode(preorder[i])
                stack.append(stack[-1].left)

            # else add right, pop off stack to know which one
            else:
                while stack and preorder[i] > stack[-1].val:
                    last = stack.pop() 
                
                last.right = TreeNode(preorder[i])
                stack.append(last.right)
        
        return root