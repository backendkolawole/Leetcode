
var findPairs = function(nums, k) {
    let lookup = {}
    
    for (let num of nums) {
        if (!lookup[num]) lookup[num] = 0
        lookup[num] += 1
    }

    let count = 0
    
    for ([key, val] of Object.entries(lookup)) {
        }

    if (k == 0) {
        for ([key, val] of Object.entries(lookup)) {
            if (val > 1) count +=1
        }
        
    }
    else {
        for ([key, val] of Object.entries(lookup)) {
            if (lookup[Number(key) + k]) count ++
        }
    }
    return count
};