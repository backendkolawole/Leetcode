var groupAnagrams = function(strs) {
    let lookup = {}

    for (let i = 0; i < strs.length; i++) {
        sorted = strs[i].split("").sort()
        if (!lookup[sorted]) lookup[sorted] = []
        lookup[sorted].push(strs[i])
    }   

    return Object.values(lookup)

};