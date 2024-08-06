/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

var binaryTreePaths = function(root) {
    let output = []
    if (!root) return output

    function traverse(node, currentPath) {
        if (!node) return ""

        currentPath += node.val
        if (!node.left && !node.right) {
            output.push(currentPath)
        }
        if (node.left) traverse(node.left, currentPath + '->')
        if (node.right) traverse(node.right, currentPath + '->')
    }
    traverse(root, '')
    return output
};