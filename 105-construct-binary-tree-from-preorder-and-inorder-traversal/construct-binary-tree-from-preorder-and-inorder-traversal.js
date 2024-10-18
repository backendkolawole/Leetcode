
var buildTree = function(preorder, inorder) {
    if (!inorder.length || !preorder.length) return null

    let root = new TreeNode(preorder[0])
    let index = inorder.indexOf(root.val)
    root.left = buildTree(preorder.slice(1, index + 1), inorder.slice(0, index))
    root.right = buildTree(preorder.slice(index + 1), inorder.slice(index + 1))
    return root

};