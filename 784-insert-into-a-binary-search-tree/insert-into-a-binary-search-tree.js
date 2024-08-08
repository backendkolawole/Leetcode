/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */


var insertIntoBST = function(root, val) {
    let newNode = new TreeNode(val)
    if (!root) {
        root = newNode
        return root
    }

    let current = root
    while (current) {
        if (current.val > val) {
            if (!current.left) {
                current.left = newNode
                break
            } 
            current = current.left

        }
        else {
            if (!current.right) {
                current.right = newNode
                break
            } 
            current = current.right

        }
    }
    return root
};