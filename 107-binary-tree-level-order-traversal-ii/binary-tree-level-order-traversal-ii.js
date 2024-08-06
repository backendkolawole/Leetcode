/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

var levelOrderBottom = function(root) {
    let output = []
    if (!root) return output
    let queue = [root]

    while (queue.length) {
        let size = queue.length
        let level = []
        for (let i = 0; i < size; i++) {
            node = queue.shift()
            level.push(node.val)
            if (node.left) queue.push(node.left)
            if (node.right) queue.push(node.right)
        }
        output.unshift(level)
    }
    return output
};