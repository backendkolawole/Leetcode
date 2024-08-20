var minimumLength = function(s) {
    let i = 0
    let j = s.length - 1

    while (i < j && s[i] == s[j]) {
        let temp = s[i]
        while (i <= j && s[i] == temp) i++
        while (i <= j && s[j] == temp) j--

    }   
    return j - i + 1

};