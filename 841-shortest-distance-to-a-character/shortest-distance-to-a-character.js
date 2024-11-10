var shortestToChar = function(s, c) {
    let prev = Infinity
    let result = new Array(s.length).fill(0)

    for (let i = 0; i < s.length; i++) {
        if (s[i] == c) {
            prev = i
        }
        else {
            result[i] = Math.abs(i - prev)
        }
    }    

    prev = Infinity
    
    for (let i = s.length - 1; i >= 0; i --) {
        if (s[i] == c) {
            prev = i
        }
        else {
            result[i] = Math.min(result[i], Math.abs(i - prev))
        }
    }
    return result
};