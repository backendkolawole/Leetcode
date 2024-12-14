var removeDuplicates = function(nums) {
    let i= 0
    let j = 0

    while (j < nums.length) {
        streak = 1

        while (j + 1 < nums.length && nums[j] == nums[j + 1]) {
            j +=1
            streak +=1
        }

        for (let a = 0; a < Math.min(streak, 2); a++) {
            nums[i] = nums[j]
            i +=1
        }
        j +=1
    }
    return i
};