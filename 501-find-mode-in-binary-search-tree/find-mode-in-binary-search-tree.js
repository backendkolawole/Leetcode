
var findMode = function(root) {
    let output = []
    if (!root) return output
    let lookup = {}
    let queue = [root]
    let mode = 0

    
    while (queue.length) {
        let node = queue.shift()

        let value = node.val
        if (!lookup[value]) lookup[value] = 0
        lookup[value] += 1
        mode = Math.max(lookup[value], mode)
        if (node.left) queue.push(node.left)
        if (node.right) queue.push(node.right)
    }  

    for (let key of Object.keys(lookup)) {
        if (lookup[key] == mode) output.push(key)
    }

    console.log(mode)

    return output
};