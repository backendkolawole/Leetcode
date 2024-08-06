/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
// use dfs
// declare three variables first, middle and last with initial values null
// define a helper dfs function 
// if the first node is not null
// if the current node is less than first node, 
// if middle is null, middle is equal to the current node 
// else last is equal to the current node
// if first is not null and middle is not none, swap the two values
// else swap the first and last 

var recoverTree = function(root) {
    let prev = null
    let first = null
    let middle = null
    let last = null

    function dfs(node) {
        if (!node) return

        if (node.left) dfs(node.left)
        if (prev != null && node.val < prev.val) {
            if (!first) {
                first = prev
                middle = node
            }
            else last = node
        }
        prev = node
        if (node.right) dfs(node.right)
    }   
    dfs(root) 
    if (first && last) [first.val, last.val] = [last.val, first.val]
    else if (first && middle) [first.val, middle.val] = [middle.val, first.val]
};