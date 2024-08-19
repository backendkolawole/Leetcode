
var reverseOnlyLetters = function(s) {
    let mySet = new Set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".split(''))
    let i = 0
    let j = s.length - 1
    s = s.split('')

    while (i < j) {
        if (!mySet.has(s[i])) i ++
        else if (!mySet.has(s[j])) j--
        else {
            [s[i], s[j]] = [s[j], s[i]]
            i ++
            j --
        }
    }    

    return s.join('')
};