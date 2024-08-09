/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */
var flatten = function(root) {
    let result = []
    if (!root) return result

    function traverse(node) {
        if (!node) return 
        result.push(node)
        if (node.left) traverse(node.left)
        if (node.right) traverse(node.right)
    }
    traverse(root)

    for (let i = 1; i < result.length; i++) {
        result[i - 1].right = result[i]
        result[i - 1].left = null
    }
    return result[0]
};