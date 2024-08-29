var maxFreq = function(s, maxLetters, minSize, maxSize) {
    let lookup = new Map()
    let output = 0
    
    for (let i = 0; i <= s.length - minSize; i++) {
        const substring = s.slice(i, i + minSize);
        if (countUnique(substring) <= maxLetters) {
            lookup.set(substring, (lookup.get(substring) || 0) + 1)
            output = Math.max(output, lookup.get(substring))
        } 
    }
    return output
};


function countUnique(str) {
    let set = new Set(str.split(''))
    return set.size
}