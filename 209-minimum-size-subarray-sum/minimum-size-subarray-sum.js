
var minSubArrayLen = function(target, nums) {
    let i = 0
    let j = 0
    let sum = 0
    let length = Infinity

    while (j < nums.length) {

        sum += nums[j]
        while (sum >= target) {
            length = Math.min(length, j - i + 1)
            sum -= nums[i]
            i++
        }

        j ++
    }    

    return length == Infinity? 0: length
};