/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

var convertBST = function(root) {
    let currentSum = 0

    function traverse(node) {
        if (!node) return
        if (node.right) traverse(node.right)
        let temp = node.val
        node.val += currentSum
        currentSum += temp
        if (node.left) traverse(node.left)

    }
    traverse(root)
    return root 

};