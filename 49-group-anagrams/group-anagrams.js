
var groupAnagrams = function(strs) {
    let lookup = {}

    for (let str of strs) {
        sorted = str.split('').sort().join('')
        if (!lookup[sorted]) {
            lookup[sorted] = []
        }
        lookup[sorted].push(str)
    }    

    return Object.values(lookup)
};