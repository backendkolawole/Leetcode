
var maxVowels = function(s, k) {
    let count = 0
    let output = 0
    let mySet = new Set("aeiou".split(''))

    for (let i = 0; i < k; i++) {
        if (mySet.has(s[i])) count ++
    }
    output = count

    for (let i = k; i < s.length; i++) {
        if (mySet.has(s[i])) count ++
        if (mySet.has(s[i - k])) count --
        output = Math.max(output, count)
    }

    return output
};