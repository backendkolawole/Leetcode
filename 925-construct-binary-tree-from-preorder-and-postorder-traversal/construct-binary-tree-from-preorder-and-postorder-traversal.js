/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

var constructFromPrePost = function(preorder, postorder) {

    function dfs(preorder, preStart, preEnd, postorder, postStart, postEnd) {
        if (preStart > preEnd) return null
        let root = new TreeNode(preorder[preStart])
        if (preStart == preEnd) return root

        // let postIndex = postStart
        // while (postorder[postIndex] != preorder[preStart + 1]) {
        //     postIndex ++
        // }

        let postIndex = postorder.indexOf(preorder[preStart + 1])
        let length = postIndex - postStart + 1
        root.left = dfs(preorder, preStart + 1, preStart + length, postorder, postStart, postIndex);
        root.right = dfs(preorder, preStart + length + 1, preEnd, postorder, postIndex + 1, postEnd - 1);
        return root
    }

    return dfs(preorder, 0, preorder.length -1, postorder, 0, preorder.length -1)
};