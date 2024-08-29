var equalSubstring = function(s, t, maxCost) {
    let output = 0
    let i = 0
    let j = 0
    let currentCost = 0

    while (j < s.length) {
        let char1 = s[j].charCodeAt(0)
        let char2 = t[j].charCodeAt(0)
        currentCost += Math.abs(char1 - char2)

        while (currentCost > maxCost) {
            currentCost -= Math.abs(s[i].charCodeAt(0) - t[i].charCodeAt(0))
            i++
        }
        output = Math.max(output, j - i + 1)
        j++
    }    
    return output
};