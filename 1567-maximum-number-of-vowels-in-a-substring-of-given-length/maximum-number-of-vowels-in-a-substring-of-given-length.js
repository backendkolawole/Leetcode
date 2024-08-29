
var maxVowels = function(s, k) {
    let count = 0
    let output = 0

    function isVowel(char) {
        let mySet = new Set("aeiou".split(''))
        return mySet.has(char)
    }    

    for (let i = 0; i < k; i++) {
        if (isVowel(s[i])) count ++
    }
    output = count

    for (let i = k; i < s.length; i++) {
        if (isVowel(s[i])) count ++
        if (isVowel(s[i - k])) count --
        output = Math.max(output, count)
    }

    return output
};