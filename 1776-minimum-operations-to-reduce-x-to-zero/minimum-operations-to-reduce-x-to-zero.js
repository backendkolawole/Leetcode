var minOperations = function(nums, x) {
    const sum = nums.reduce((a, b)=> a + b)
    const target = sum - x
    let windowSize = - 1
    let i = 0
    let j = 0
    let currentSum = 0
    while (j < nums.length) {
        currentSum += nums[j]

        while (currentSum > target) {
            currentSum -= nums[i]
            i ++
        }

        if (currentSum == target) {
            windowSize = Math.max(windowSize, j - i + 1)
        }


        j ++
    }  
    return windowSize == -1 ? windowSize: nums.length - windowSize
};