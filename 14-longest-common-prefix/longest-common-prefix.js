var longestCommonPrefix = function(strs) {
    strs = strs.sort()

    let first = strs[0]
    let last = strs.at(-1)

    if (!first) return ""

    if (first == last) return last

    for (let i = 0; i < last.length; i++) {
        if (first[i] != last[i]) return first.slice(0, i)
    }
    
    return first


};