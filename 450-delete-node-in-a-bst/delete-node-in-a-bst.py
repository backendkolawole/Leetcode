
class Solution:

    def findMin(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)        
        else:
            if not root.left and not root.right:
                root = None
            elif not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                temp = self.findMin(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)

        return root
            

            