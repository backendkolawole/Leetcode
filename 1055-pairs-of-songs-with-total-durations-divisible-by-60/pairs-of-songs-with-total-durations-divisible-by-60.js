
var numPairsDivisibleBy60 = function(time) {
    let lookup = {}
    let count = 0
    let k = 60
    
    for (let x of time) {
        let remainder = x % k
        count += lookup[(k - remainder) % k] || 0
        if (!lookup[remainder]) lookup[remainder] = 0
        lookup[remainder] += 1
    }
    
    return count    
};