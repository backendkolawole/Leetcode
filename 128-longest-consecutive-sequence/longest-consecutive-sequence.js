// store the elements of nums in a set
// iterate through nums
// if the current num is the first in its sequence
// while the next number in the sequence is present in the set
// count the consecutive elements sequence

var longestConsecutive = function(nums) {
    let mySet = new Set(nums)
    let max = 0

    for (let num of nums) {
        if (!mySet.has(num - 1)) {
            let count = 1
            while (mySet.has(num + 1)) {
                count += 1
                num ++
            }
            max = Math.max(max, count)
        }
    }
    return max
};