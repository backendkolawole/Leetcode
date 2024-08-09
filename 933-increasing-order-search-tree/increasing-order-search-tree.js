/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

var increasingBST = function(root) {
    let inorder = []
    if (!root) return inorder

    function traverse(node) {
        if (!node) return 
        if (node.left) traverse(node.left)
        inorder.push(new TreeNode(node.val))
        if (node.right) traverse(node.right)
    }
    traverse(root)

    for (let i = 1; i < inorder.length; i++) {
        inorder[i - 1].right = inorder[i]
        inorder[i - 1].left = null
    }
    return inorder[0]
};

